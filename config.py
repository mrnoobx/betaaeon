# REQUIRED CONFIG
BOT_TOKEN = "7881934453:AAH38A4dHvwn1hU8HMziaTlFeJ-lZFH4SmI"
OWNER_ID = 7442532306
TELEGRAM_API = 29382018
TELEGRAM_HASH = "4734a726c04620c61ec0a28a1ae0d57f"

# SEMI-REQUIRED, WE SUGGEST TO FILL IT FROM MONGODB
DATABASE_URL = "mongodb+srv://mrnoobx:DAZCdTczVWyECi04@cluster0.sedgwxy.mongodb.net/?retryWrites=true&w=majority"

# OPTIONAL CONFIG
TG_PROXY = {}
USER_SESSION_STRING = ""
DOWNLOAD_DIR = "/usr/src/app/downloads/"
CMD_SUFFIX = ""
AUTHORIZED_CHATS = "-1002180300815"
SUDO_USERS = ""
DEFAULT_UPLOAD = "rc"
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SUBSTITUTE = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# INKYPINKY
DELETE_LINKS = False
FSUB_IDS = "-1002310978225"
TOKEN_TIMEOUT = 0
LOGIN_PASS = ""  # Set a password to enable login feature
PAID_CHANNEL_ID = 0
PAID_CHANNEL_LINK = ""
SET_COMMANDS = True
METADATA_KEY = ""
LOG_CHAT_ID = -1002428562251
LEECH_FILENAME_CAPTION = ""
HYDRA_IP = ""
HYDRA_API_KEY = ""
INSTADL_API = ""
MEDIA_STORE = False

# Media Tools Settings
MEDIA_TOOLS_ENABLED = True  # Enable/disable Media Tools feature

# Music Search
MUSIC_SEARCH_CHATS = []  # List of chat IDs to search for music

# GDrive Tools
GDRIVE_ID = ""
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# Mega credentials
MEGA_EMAIL = ""
MEGA_PASSWORD = ""

# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    },
]

# Update
UPSTREAM_REPO = "https://github.com/Mrlabani/Aeon-MLTB"
UPSTREAM_BRANCH = "beta"

# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
MEDIA_GROUP = False
USER_TRANSMISSION = False
HYBRID_LEECH = False
LEECH_FILENAME_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_FILENAME = ""
LEECH_DUMP_CHAT = "-1002428562251"
THUMBNAIL_LAYOUT = "https://i.ibb.co/ksz5ZH1y/17aeaf02bdc7.jpg"

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 80
WEB_PINCODE = False

# Queueing system
QUEUE_ALL = 5
QUEUE_DOWNLOAD = 8
QUEUE_UPLOAD = 5

# Resource Management
FFMPEG_MEMORY_LIMIT = 2048  # Memory limit in MB (0 = no limit)
FFMPEG_CPU_AFFINITY = (
    ""  # CPU cores to use (e.g., "0-3" or "0,2,4,6"), empty = all cores
)
FFMPEG_DYNAMIC_THREADS = True  # Dynamically adjust thread count based on system load

# Auto Restart Settings
AUTO_RESTART_ENABLED = False  # Enable/disable automatic bot restart
AUTO_RESTART_INTERVAL = 12  # Restart interval in hours

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0
