import asyncio
import os
import interactions as it
from interactions import Client, Button, SelectMenu, ActionRow
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC

from settings.config import *
from interactions.ext.wait_for import wait_for, setup,wait_for_component

import pymongo


presence = it.PresenceActivity(name="Calculator", type=it.PresenceActivityType.GAME)
bot = Client(token=TOKEN,disable_sync=False,presence=it.ClientPresence(activities=[presence]))


#logging.basicConfig(level=logging.DEBUG)



setup(bot)

@bot.event
async def on_ready():
    bot_name = bot.me.name
    print(f"Logged in as {bot_name}!")


bot.load("cogs.updater")
bot.load("cogs.payment")


bot.start()