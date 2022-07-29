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
        self.logs = woodcutter
        self.ores = miner
        self.relics = crafter
        self.bars = smither
        self.fish_salt = fisher
        self.magic = tailor
        self.categories = { "logs":self.logs,
                            "ores":self.ores,
                            "relics":self.relics,
                            "bars":self.bars,
                            "fish_salt": self.fish_salt,
                            "magic": self.magic
                        }
        return
    
    def insert_item(self,category:str,item:str,value:int):
        """insert new item to database"""
        return
    
    def update_item(self,item:str,new_value:int):
        """update chosen item in database with a given value"""
        return
    
    def delete_item(self,item:str):
        """delete chosen item from database"""
        return
    
    def get_items_list(self):
        """view list of item-value stored in database"""
        return
    






