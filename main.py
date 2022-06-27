import os
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
import datetime

import time
import math
from settings.config import TOKEN

import logging



#presence = it.PresenceActivity(name="Calculator", type=it.PresenceActivityType.GAME)
bot = Client(token=TOKEN,disable_sync=False)
logging.basicConfig(level=logging.DEBUG)

@bot.event
async def on_ready():
    bot_name = bot.me.name
    print(f"Logged in as {bot_name}!")

#cogs = ["guilds"]
#for cog in cogs:
bot.load("cogs.calcs")
print("calcs loaded")

bot.start()
