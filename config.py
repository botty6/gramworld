# (©)t.me/CodeFlix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token from @BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "0"))  # Safe default to avoid crash

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your DB channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))  # Fixed missing parenthesis

# Name of the owner
OWNER = os.environ.get("OWNER", "iBOXTVADS")

# Owner Telegram ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6124171612"))

# Port
PORT = os.environ.get("PORT", "8030")

# Database connection URI
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "bot13")

# Force subscription channels
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002311266823"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002311266823"))

# Telegram bot workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello Pirate!! {first}\n\n ɪ Store files and users can access them through clicking special buttons. </b>"
)

# Admins list
try:
    ADMINS = [6124171612]
    for x in os.environ.get("ADMINS", "762308466").split():
        admin_id = int(x)
        if admin_id not in ADMINS:
            ADMINS.append(admin_id)
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force subscription message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ using any button below ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>"
)

# Optional custom caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Protect forwarded content
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"

# Disable share button on channel posts
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == "True"

# Bot statistics text
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Pirate ! ʏᴏᴜ Need to be myy Owner to do that !!"

# Include OWNER_ID and main admin in ADMINS
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)
if 6124171612 not in ADMINS:
    ADMINS.append(6124171612)

# Log file configuration
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50_000_000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Logger function
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
