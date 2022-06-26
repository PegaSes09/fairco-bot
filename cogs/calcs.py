import interactions
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
import datetime
from datetime import datetime
import asyncio

from settings.config import *



class Recruit(interactions.Extension):

    def __init__(self,client : Client) -> None:
        self.bot = client
        self.prices = prices
        self.rates = rates
        
        return













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
        ]
    )
    async def pay(ctx: CC,worker: str ="",amount: str ="" resource: str =""):
        if worker == "" or amount == "" or resource == "" :
            await ctx.send("a parameter is missing")
        else:
            rate = rates[worker.lower()]
            price = prices[resource.lower()]
            payment = int(amount) * price * rate
            msg = "payment is "+ {:,}.format(payment) + " gold coins."
            await ctx.send(msg)

    @interaction.extension_autocomplete("pay", "resource")
    async def resource_autocomplete(ctx: CC, value: str = ""):
        resources_prices = list(prices.keys())
        choices = [
            it.Choice(name=price, value=price) for price in resources_prices if value in price
        ] 
        await ctx.populate(choices)
        
    @interaction.extension_autocomplete("pay", "tier")
    async def worker_autocomplete(ctx: CC, value: str = ""):
        workers = list(rates.keys())
        choices = [
            it.Choice(name=worker, value=worker) for worker in workers if value in worker
        ] 
        await ctx.populate(choices)


def setup(client : Client):
    Recruit(client)
