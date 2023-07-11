# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "19902008"))
API_HASH = os.environ.get("API_HASH", "d973fa8af375787c85dd6d2dfac94d7e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5862295422:AAEVI5YXLv_O_jq0jjSCZpM7xCj8-5iWwss")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5204439926")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "URL_shortner")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://moviesdudebot:MDbots@cluster0.y4gwugw.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5204439926")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5204439926)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001512187826")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MD_Bots") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
