import os

"""the bot token saved in env vars as 'TOKEN' """
TOKEN = os.getenv("TOKEN")

prices = {
        "pine log": 2000,
        "dead log": 2000,
        "birch log": 2000,
        "apple wood": 2000,
        "willow log": 4000,
        "oak log": 4000,
        "chestnut log": 5000,
        "maple log": 5000,
        "olive log": 7000,
        "palm wood": 7000,
        "magic log": 4000,
        
        "accuracy relic": 3000,
        "guarding relic": 3000,
        "healing relic": 3000,
        "wealth relic": 3000,
        "power relic": 5000,
        "nature relic": 5000,
        "fire relic": 5000,
        "damage relic": 6000,
        "leeching relic": 4000,
        "experience relic": 13000,
        "cursed relic": 3000,
        "ice relic": 3000,
        
        "coal": 2500,
        "crimsteel ore": 2500,
        "gold ore": 2000,
        "mythan ore": 6000,
        "cobalt ore": 8000,
        "varaxium ore": 10000,
        "magic ore": 9000,
        
        "crimsteel bar": 15000,
        "gold bar": 600000,
        "mythan bar": 80000,
        "cobalt bar": 90000,
        "varaxium bar": 100000,
        "magic bar": 100000,
        
        "salt": 3000,
        "pink salt": 6000,
        "black salt": 4000,
        "scallop": 4000,
        "grasshopper": 9000,
        "bass": 33000,
        
        "magic essence": 800,
        "paper": 700,
        "leather": 3000,
        "book": 10000
        
        }










woodcutter = [
        "pine log",
        "dead log",
        "birch log",
        "apple wood",
        "willow log",
        "oak log",
        "chestnut log",
        "maple log",
        "olive log",
        "palm wood",
        "magic log"
        ]
        
crafter = [
        "accuracy relic",
        "guarding relic",
        "healing relic",
        "wealth relic",
        "power relic",
        "nature relic",
        "fire relic",
        "damage relic",
        "leeching relic",
        "experience relic",
        "cursed relic",
        "ice relic"
        ]
        
miner = [
        "coal",
        "crimsteel ore",
        "gold ore",
        "mythan ore",
        "cobalt ore",
        "varaxium ore",
        "magic ore"
        ]
        
smither = [
        "crimsteel bar",
        "gold bar",
        "mythan bar",
        "cobalt bar",
        "varaxium bar",
        "magic bar"
        ]
        
fisher = [
        "salt",
        "pink salt",
        "black salt",
        "scallop",
        "grasshopper",
        "bass"
        ]

tailor = [
        "magic essence",
        "paper",
        "leather",
        "book"
        ]

jobs = [woodcutter,crafter,miner,smither,fisher,tailor]

job_list = ["woodcutter","crafter","miner","smither","fisher","tailor"]

worker_tiers = [
        "worker",
        "elite worker",
        "goat worker",
        "supreme worker",
        "immortal worker",
        "knight of workers"
        ]  


        
        
rates = {
    "worker": 99,
    "elite worker": 99.1,
    "goat worker": 99.2,
    "supreme worker": 99.3,
    "immortal worker": 99.4,
    "knight of workers": 99.5
}


resources_list = {
    "logs" : [
        "pine log",
        "dead log",
        "birch log",
        "apple wood",
        "willow log",
        "oak log",
        "chestnut log",
        "maple log",
        "olive log",
        "palm wood",
        "magic log"
        ]
        
    "relics" : [
        "accuracy relic",
        "guarding relic",
        "healing relic",
        "wealth relic",
        "power relic",
        "nature relic",
        "fire relic",
        "damage relic",
        "leeching relic",
        "experience relic",
        "cursed relic",
        "ice relic"
        ]
        
    "ores" : [
        "coal",
        "crimsteel ore",
        "gold ore",
        "mythan ore",
        "cobalt ore",
        "varaxium ore",
        "magic ore"
        ]
        
    "bars" : [
        "crimsteel bar",
        "gold bar",
        "mythan bar",
        "cobalt bar",
        "varaxium bar",
        "magic bar"
        ]
        
    "fish_salt" : [
        "salt",
        "pink salt",
        "black salt",
        "scallop",
        "grasshopper",
        "bass"
        ]

    "magic" : [
        "magic essence",
        "paper",
        "leather",
        "book"
        ]
    }


