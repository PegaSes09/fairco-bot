from ast import arg
from pprint import pprint
import interactions
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC

import asyncio
import interactions.ext.wait_for
from interactions.ext.wait_for import wait_for_component, wait_for

from settings.config import *
from db_helper import *



class MasterUpdater(interactions.Extension):

    def __init__(self,client : Client) -> None:
        self.bot = client
        self.resources_list = retrieve("resources_list")
        self.prices = retrieve("prices_list")

        self.commit_button  = Button(
            label="Commit",
            custom_id="commit_btn",
            style=ButtonStyle.SUCCESS
        )
        self.discard_button  = Button(
            label="Discard",
            custom_id="discard_btn",
            style=ButtonStyle.DANGER
        )
        self.delete_button  = Button(
            label="Delete",
            custom_id="delete_btn",
            style=ButtonStyle.DANGER
        )


        return

    def insert_item(self,category:str,item:str,value:int):
        """insert new item to database"""
        current_prices = retrieve("prices_list")
        current_prices[item]=value
        self.prices[item]=value
        inserted1 = update("prices_list",jsing(current_prices))
        current_resources = retrieve("resources_list")
        if item not in current_resources:
            current_resources[category].append(item)
            self.resources_list[category].append(item)
        inserted2 = update("resources_list",jsing(current_resources))

        return all([inserted1,inserted2])
    
    def update_item(self,item:str,new_value:int):
        """update chosen item in database with a given value"""
        current_prices = retrieve("prices_list")
        current_prices[item]=new_value
        self.prices[item]=new_value
        inserted = update("prices_list",jsing(current_prices))
        return inserted
    
    def delete_item(self,category:str,item:str):
        """delete chosen item from database"""
        current_prices = retrieve("prices_list")
        current_prices.pop(item)
        self.prices.pop(item)
        inserted1 = update("prices_list",jsing(current_prices))

        current_resources = retrieve("resources_list")
        current_resources[category].remove(item)
        self.resources_list[category].remove(item)
        inserted2 = update("resources_list",jsing(current_resources))

        return all([inserted1,inserted2])
    
    def get_items_prices(self,category:str):
        """view list of item-price of given category from database"""
        items_prices = {}
        resources = self.resources_list[category]
        for resource in resources :
            items_prices[resource] = self.prices[resource]
        return items_prices
    
    def make_menu(self,options_list:list[str],ph:str,id:str):
        """create SelectMenu from given parameters"""
        menu_options = []
        for option in options_list:
            menu_options.append(it.SelectOption(label=option,value=option))
        menu = it.SelectMenu(options=menu_options,
                            placeholder=ph,
                            custom_id=id
                            )
        return menu

    def make_choices(choices_list:list[str]):
        """create SelectOption from given parameters"""
        choices = []
        for choice in choices_list:
            choices.append(it.Choice(name=choice,value=choice))
        return choices

    async def insert_modal(self,ctx:CC):
        resource_name_ip = TextInput(
            label="Resource name : ",
            placeholder="Enter resource name",
            style=TextStyleType.PARAGRAPH,
            custom_id="resource_name",
            required=True
            )
        resource_price_ip = TextInput(
            label="Resource name : ",
            placeholder="Enter resource's price",
            style=TextStyleType.SHORT,
            custom_id="resource_price",
            required=True
            )
        modal = Modal(
                title="Inserting a new resource to database",
                components= [resource_name_ip,resource_price_ip],
                custom_id="insert_modal"
            )
        await ctx.popup(modal)




    @interactions.extension_command(
        name="resource", 
        description="modify the resource database", 
        options= [
            it.Option(
                name="update",
                description="update a resource price",
                type=it.OptionType.SUB_COMMAND,
                options=[
                    it.Option(
                        name="category",
                        description="the resource's category",
                        type=it.OptionType.STRING,
                        choices = make_choices(categories),
                        required=True)
                        ]
                    ),
            it.Option(
                name="insert",
                description="insert a new resource into database",
                type=it.OptionType.SUB_COMMAND,
                options=[
                    it.Option(
                        name="category",
                        description="the resource's category",
                        type=it.OptionType.STRING,
                        choices = make_choices(categories),
                        required=True)
                        ]
                    ),
            it.Option(
                name="delete",
                description="delete a resource from database",
                type=it.OptionType.SUB_COMMAND,
                options=[
                    it.Option(
                        name="category",
                        description="the resource's category",
                        type=it.OptionType.STRING,
                        choices = make_choices(categories),
                        required=True)
                        ]
                    ),
            it.Option(
                name="view",
                description="view resources of given category",
                type=it.OptionType.SUB_COMMAND,
                options=[
                    it.Option(
                        name="category",
                        description="the resource's category",
                        type=it.OptionType.STRING,
                        choices = make_choices(categories),
                        required=True)
                        ]   
                    )
                ],
        default_member_permissions=it.Permissions.ADMINISTRATOR
            )
    async def resource(self,ctx: CC, sub_command: str, category: str):
        resource_price_ip = TextInput(
                label="Resource's price : ",
                placeholder="Enter resource's price",
                style=TextStyleType.SHORT,
                custom_id=f"{category}_resource_price",
                required=True
                )
        resource_name_ip = TextInput(
                label="Resource's name : ",
                placeholder="Enter resource name",
                style=TextStyleType.PARAGRAPH,
                custom_id=f"{category}_resource_name",
                required=True
                )

        async def check(comp_ctx):
            if int(comp_ctx.author.user.id) == int(ctx.author.user.id):
                return True
            await ctx.send("I wasn't asking you!", ephemeral=True)
            return False

        if sub_command == "insert":
            insert_modal = Modal(
                    title="Inserting a new resource to database",
                    components= [resource_name_ip,resource_price_ip],
                    custom_id="insert_modal"
                )
            await ctx.popup(insert_modal)
            modal_ctx: interactions.CommandContext = await wait_for(self.bot, name="on_modal", timeout=60)
            
        elif sub_command == "update":
            resource_menu = self.make_menu(self.resources_list[category],"Select resource !","rsc_menu")
            await ctx.send("Select resource : ",components= [resource_menu])
            try:
                rsc_ctx = await self.bot.wait_for_component( components=resource_menu, check=check, timeout=60) 
                selected_rsc =  rsc_ctx.data.values[0]
                selected_rsc = selected_rsc.replace(" ","-")
                resource_price_ip.custom_id=f"{category}_{selected_rsc}_resource_name"
                selected_rsc = selected_rsc.replace("-"," ")
                update_modal = Modal(
                    title=f"Updating {selected_rsc}'s price [{self.prices[selected_rsc]}]",
                    components=[resource_price_ip],
                    custom_id="update_modal"
                )
                await rsc_ctx.popup(update_modal)
            except asyncio.TimeoutError: 
                await ctx.edit("timed out!",components=[]) 
            
        elif sub_command == "delete":
            resource_menu = self.make_menu(self.resources_list[category],"Select Resource !","rsc_menu")
            self.delete_button.disabled = True
            await ctx.send("Select resource : ",components=[resource_menu])

            try:
                rsc_ctx: CC = await self.bot.wait_for_component( components=resource_menu, check=check, timeout=60) 
                selected_rsc =  rsc_ctx.data.values[0]
                deleted = self.delete_item(category,selected_rsc)
                state = "success" if deleted else "fail"
                await ctx.edit(f"deleting {selected_rsc} was a {state}",components=[])
            except asyncio.TimeoutError: 
                await ctx.edit("timed out!",components=[]) 
            
        elif sub_command == "view":
            category_s_resources = self.get_items_prices(category)
            msg = ""
            for rsc in category_s_resources:
                msg = msg + rsc + ' : ' + "{:,}".format(category_s_resources[rsc]) + '\n' 
            await ctx.send(msg)
            
            
    @interactions.extension_modal("insert_modal")
    async def insert_response(self,ctx:CC,*args):
        
        id:str = ctx.data.components[0].components[0].custom_id
        category = id.split("_")[0]

        async def check(comp_ctx):
            if int(comp_ctx.author.user.id) == int(ctx.author.user.id):
                return True
            await ctx.send("I wasn't asking you!", ephemeral=True)
            return False

        name = args[0]
        price = "{:,}".format(int(args[1]))
        msg = f"you entered [{name} : {price}]"
        msg = msg + '\n' + "commit ?"
        await ctx.send(msg,components=[self.commit_button])
        try:
            commit_ctx: CC = await self.bot.wait_for_component( components="commit_btn", check=check, timeout=20) 
            inserted = self.insert_item(category,name,int(args[1]))
            #if inserted:
            await ctx.edit(f"input saved to database",embeds=[], components=[]) #do stuffs here
        except asyncio.TimeoutError: 
            await ctx.edit("timed out!",components=[])


    @interactions.extension_modal("update_modal")
    async def update_response(self,ctx:CC,*args):
        id:str = ctx.data.components[0].components[0].custom_id
        category = id.split("_")[0]
        name = id.split("_")[1].replace("-"," ")

        async def check(comp_ctx):
            if int(comp_ctx.author.user.id) == int(ctx.author.user.id):
                return True
            await ctx.send("I wasn't asking you!", ephemeral=True)
            return False


        price = int(args[0])
        msg = f"you entered [{name} : { '{:,}'.format(price)}]"
        msg = msg + '\n' + "commit ?"
        await ctx.send(msg,components=[self.commit_button])
        try:
            commit_ctx: CC = await self.bot.wait_for_component( components="commit_btn", check=check, timeout=20) 
            inserted = self.update_item(name,int(args[0]))
            #if inserted:
            await commit_ctx.edit(f"input updated to database",embeds=[], components=[]) #do stuffs here
        except asyncio.TimeoutError: 
            await ctx.edit("timed out!",components=[])

#    @interactions.extension_listener()
#    async def on_component(self,ctx:CPC,*args):
#        if ctx.custom_id.endswith("delete_btn"):
#
#            deleted = False
#            category = ctx.custom_id.split("_")[0]
#            selected_rsc = ctx.custom_id.split("_")[1].replace("-"," ")
#            try:
#                deleted = self.delete_item(category,selected_rsc)
#                await ctx.send(f"{selected_rsc} deleted successfelly",components=[])
#            except Exception as e:
#                print(e)





def setup(client : Client):
    MasterUpdater(client)
