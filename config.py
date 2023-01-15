import os

import re

id_pattern = re.compile(r'^.\d+$')

# temp db for banned 

class temp(object):

    BANNED_USERS = []

    BANNED_CHATS = []

    ME = None

    CURRENT=int(os.environ.get("SKIP", 2))

    CANCEL = False

    MELCOW = {}

    U_NAME = None

    B_NAME = None

class Config(object):

    # get a token from @BotFather

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945346287:AAE3gmyeGs-oK2UxcgbTDWjr48an4iv-oSY")

    # The Telegram API things

    # Get these values from my.telegram.org

    APP_ID = int(os.environ.get("APP_ID", 22681384))

    API_HASH = os.environ.get("API_HASH", "14ae45755537c723aab0564a80d723a9")

    # Array to store users who are authorized to use the bot

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5468192421").split())

    # the download location, where the HTTP Server runs

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size

    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests

    CHUNK_SIZE = 128

    # Generate screenshots for file after uploading

    # Defaults to True

    SCREENSHOTS = os.environ.get("SCREENSHOTS", "True")

    # default thumbnail to be used in the videos

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://telegra.ph/file/8eddfc57dde92ec6e288e.jpg")

    # proxy for accessing youtube-dl in GeoRestricted Areas

    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    

    # Update channel for Force Subscribe

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001523739263")

    # maximum message length in Telegram

    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess

    PROCESS_MAX_TIMEOUT = int(os.environ.get("TIME_LIMIT", 30))

    

    # dict to hold the ReQuest queue

    ADL_BOT_RQ = {}

    # watermark file

    DEF_WATER_MARK_FILE = "@All_Movie_Rocker"

    # Sql Database url

    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")

    

    # Database Name

    DATABASE_NAME = os.environ.get('DATABASE_NAME', "URL-BOT")

    

    # Log channel for banning spammers

    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001860694129")

    

    # space to divide admins

    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMINS', '5468192421').split()]

    

    # Sql Database url

    DB_URI = os.environ.get("DATABASE_URL", "postgres://yukjcgin:NcbdNkUa32FRsdJYjWbxroFcMVRGKHuG@arjuna.db.elephantsql.com/yukjcgin")

    

    SUPPORT_CHAT = os.environ.get('SUPPORT_CHAT', '@All_Movie_Rocker')

    

    # Banned Unwanted Members..

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
