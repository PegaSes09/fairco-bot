import interactions
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
import datetime
from datetime import datetime
import asyncio

from settings.config import *



class Calc(interactions.Extension):

    def __init__(self,client : Client) -> None:
        self.bot = client
        self.prices = prices
        self.rates = rates
        
        return











    @interactions.extension_command(name="ping",description="show ping")
    async def ping(self,ctx:CC):
        await ctx.send(f"pong ! {round(self.bot.latency)} ms.")

    @interactions.extension_command(
        name="pay",
        description="calculate the worker's payment",
        options=[
            it.Option(
                type=it.OptionType.STRING,
                name="tier",
                description="the worker's tier",
                required=True,
                autocomplete=True,
            ),
            it.Option(
                type=it.OptionType.STRING,
                name="amount",
                description="the resource's amount",
                required=True,
                autocomplete=False,
            ),
            it.Option(
                type=it.OptionType.STRING,
                name="resource",
                description="the resource used",
                required=True,
                autocomplete=True,
            )
        ],
        scope = [839662151010353172,922854662141526037,712120246915301429]
    )
    async def pay(self,ctx: CC, worker: str, amount: str, resource: str):
        if not int(ammount) :
            await ctx.send("amount must be a number")
        else:
            rate = self.rates[worker.lower()]
            price = self.prices[resource.lower()]
            payment = int(amount) * price * rate / 100
            msg = f"payment is {payment:,} gold coins."
            await ctx.send(msg)

    @interactions.extension_autocomplete("pay", "resource")
    async def resource_autocomplete(self,ctx: CC, value: str = ""):
        resources_prices = list(self.prices.keys())
        choices = [
            it.Choice(name=price, value=price) for price in resources_prices if value in price
        ] 
        await ctx.populate(choices)
        
    @interactions.extension_autocomplete("pay", "tier")
    async def worker_autocomplete(self,ctx: CC, value: str = ""):
        workers = list(self.rates.keys())
        choices = [
            it.Choice(name=worker, value=worker) for worker in workers if value.lower() in worker.lower()
        ] 
        await ctx.populate(choices)


def setup(client : Client):
    Calc(client)
