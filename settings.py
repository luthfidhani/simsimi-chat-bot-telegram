import os
from dotenv import load_dotenv

load_dotenv()

BOT_URL = os.getenv("BOT_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_OWNER_ID = os.getenv("BOT_OWNER_ID")
WEBHOOK_URL = f"{BOT_URL}/{BOT_TOKEN}"