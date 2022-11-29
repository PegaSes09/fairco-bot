import os

"""the bot token saved in env vars as 'TOKEN' """
TOKEN = os.getenv("TOKEN")
"""the database connection string saved in env vars as 'DB_URL' """
DB_URL = os.getenv("DB_URL")


job_list = ["woodcutter","crafter","miner","smither","fisher","tailor"]
job_rsc = {"woodcutter":"logs","crafter":"relics","miner":"ores","smither":"bars","fisher":"fish_salt","tailor":"magic"}
categories = [ "logs",
                "ores",
                "relics",
                "bars",
                "fish_salt",
                "magic"
            ] 