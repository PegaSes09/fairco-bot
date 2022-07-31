import asyncio
import os
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
from db_helper import retrieve

from settings.config import *
from interactions.ext.wait_for import wait_for, setup,wait_for_component

import logging




#presence = it.PresenceActivity(name="Calculator", type=it.PresenceActivityType.GAME)
bot = Client(token=TOKEN,disable_sync=False)
#logging.basicConfig(level=logging.DEBUG)



setup(bot)

@bot.event
async def on_ready():
    bot_name = bot.me.name
    print(f"Logged in as {bot_name}!")

def make_menu(items:list,ph:str,ci:str):
    options = []
    for item in items:
        options.append(it.SelectOption(label=item,value=item))
    menu = it.SelectMenu(options=options,
                            placeholder=ph,
                            custom_id=ci)
    return menu

def update_menu(menu:it.SelectMenu,selected_option:str):
    menu.default = selected_option
    return menu

def disable_menu(items_list:list,menu:SelectMenu,option:str):
    id = items_list.index(option)

    menu.options[id].default = True
    menu.disabled = True
    return menu

def disable_button(btn:Button):
    btn.disabled=True
    return btn

def make_rsc_menu(menu:SelectMenu,items_list:list):
    options = []
    rscs = items_list
    for i in rscs:
        options.append(it.SelectOption(label=i.lower(),value=i.lower()))
    menu.options=options
    return menu

def calc(amount:int,rsc:str,tier:str):
    prices_list = retrieve("prices_list")
    price = prices_list[rsc.lower()]
    rate = rates[tier]
    payment = amount * price * rate / 100
    return int(payment)










@bot.command(   name="pay", 
                description="calculate worker's payment", 
                scope = [839662151010353172,712120246915301429], 
                options=[it.Option( name="job",
                                    description="the worker's job",
                                    type=it.OptionType.STRING,
                                    required=True,
                                    choices=[
                                            it.Choice(name="woodcutter",value="woodcutter"),
                                            it.Choice(name="crafter",value="crafter"),
                                            it.Choice(name="miner",value="miner"),
                                            it.Choice(name="smither",value="smither"),
                                            it.Choice(name="fisher",value="fisher"),
                                            it.Choice(name="tailor",value="tailor")
                                            ]
                                        ),  
                        it.Option( name="amount",
                                    description="resource's amount",
                                    type=it.OptionType.STRING,
                                    required=True,
                                    autocomplete=False )
                        ],
                default_member_permissions=it.Permissions.ADMINISTRATOR
            )
async def pay(ctx:CC,job:str,amount:str):
    selected_tier = "worker"
    selected_job = job
    selected_rsc = "pine log"

    resources = retrieve("resources_list")
    rsc_list = resources[job_rsc[job]]


    await ctx.defer()

    try:
        amount_int = int(amount)
    except ValueError: 
        await ctx.send("amount must be a number without letters",ephemeral=True) 

    tier_menu = make_menu(items=worker_tiers,ph="Choose a worker tier",ci="tier_menu")
    rsc_menu = make_menu(items=rsc_list,ph="Choose the resource",ci="rsc_menu")
    calc_btn=it.Button(label="Calc",style=it.ButtonStyle.SUCCESS,custom_id="calc_btn")

    btns_row = ActionRow(components=[calc_btn])

    default_rows = [ActionRow(components=[tier_menu]),ActionRow(components=[rsc_menu]),btns_row]

    await ctx.send("Calculating ...",embeds=[], components=default_rows)
    async def check(comp_ctx):
        if int(comp_ctx.author.user.id) == int(ctx.author.user.id):
            return True
        await ctx.send("I wasn't asking you!", ephemeral=True)
        return False
    try:
        tier_ctx: CC = await bot.wait_for_component( components=tier_menu, check=check, timeout=60) 
        selected_tier =  tier_ctx.data.values[0]
        default_rows[0] = ActionRow(components = [disable_menu(worker_tiers, tier_menu, selected_tier)])
        await tier_ctx.edit("Calculating ...",embeds=[], components=default_rows)
    except asyncio.TimeoutError: 
        await ctx.edit("timed out!",components=[]) 
    
    try:
        rsc_ctx: CC = await bot.wait_for_component( components=rsc_menu, check=check, timeout=60) 
        selected_rsc =  rsc_ctx.data.values[0]
        default_rows[1] = ActionRow(components = [disable_menu(rsc_list, rsc_menu, selected_rsc)])
        await rsc_ctx.edit("Calculating ...",embeds=[], components=default_rows)
    except asyncio.TimeoutError: 
        await ctx.edit("timed out!",components=[]) 
    
    try:
        btn_ctx: CC = await bot.wait_for_component( components=calc_btn, check=check, timeout=60) 
        default_rows[1] = ActionRow(components = [disable_button(calc_btn)])
        result = calc(int(amount),selected_rsc,selected_tier)
        text = f"Payment for {int(amount):,} {selected_rsc} for {selected_tier} is {result:,}"
        await btn_ctx.edit(text,embeds=[], components=[])
    except asyncio.TimeoutError: 
        await ctx.edit("timed out!",components=[]) 

#cogs = ["guilds"]
#for cog in cogs:
bot.load("cogs.updater")
print("updater loaded")

bot.start()
