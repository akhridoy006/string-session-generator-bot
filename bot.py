import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client
from pyromod import listen


API_ID = int(os.environ.get("26397851", 0))
API_HASH = os.environ.get("bb9c1429fc139805d7e043d097454b68", None)
BOT_TOKEN = os.environ.get("7694366211:AAEtV5hSvpY8AuFZHta9F37mMT08G7IMkk0", None)
API_KEY = os.environ.get("API_KEY", None)


def main():
    app = Client(name="String Session",
                 bot_token = BOT_TOKEN,
                 api_id = API_ID,
                 api_hash = API_HASH,
                 plugins = dict(root="plugins"),
                 workers = 100,
                 sleep_threshold = 15)

    app.run()


if __name__ == "__main__":
    main()
