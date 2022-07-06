import interactions
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC

import asyncio
import interactions.ext.wait_for
from interactions.ext.wait_for import wait_for_component, setup

from settings.config import *



class Calc(interactions.Extension):

    def __init__(self,client : Client) -> None:
        self.bot = client
        self.prices = prices
        self.rates = rates
        self.jobs = jobs
        self.job_list = job_list
        self.tiers = worker_tiers

        return
    









    @interactions.extension_command(name="ping",description="show ping")
    async def ping(self,ctx:CC):
        await ctx.send(f"pong ! {round(self.bot.latency)} ms.")

    
    
    

    


#def setup(client : Client):
#    Calc(client)
