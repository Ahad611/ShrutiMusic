# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ⚙️ CONFIGURATION FILE | Powered By @WTF_WhyMeeh & @ShrutiBots
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📲 Telegram & API Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = int(os.getenv("28209312"))
API_HASH = os.getenv("89def84a7894bb696ff20174c86889a4")
BOT_TOKEN = os.getenv("7866554017:AAHZ_0S-R_-veYpyQLYmvhWIxSIBAaj53tE")
OWNER_ID = int(os.getenv("7710841624", None))
OWNER_USERNAME = os.getenv("x7Ahad", "WTF_WhyMeeh")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️ Database & Deployment Configs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = os.getenv("mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan", None)
LOG_GROUP_ID = int(os.getenv("-1002740659166", None))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Git & Update Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = os.getenv("https://github.com/Ahad611/ShrutiMusic", "https://github.com/NoxxOP/ShrutiMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/Addiction_World")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/+Ay_8Q6xrMbtkOTll")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (in bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Developer Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧵 Session Strings (Pyrogram V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("BQCOaU4AxARKjnw05xbtfoloNJ-aoETw3cDYx9Zb0-MSff9U9gRd2jzmYDN1mUvTxR7YW_Z6QCrzexzmncDt9kZ671bEtM7vju2MF907KNDJtRbM7A0coTWwk5x-r0YZVBTkvJqgvKnn3tPc6aKuwe3ntj_fTh4U3qeoymvdVLAySoqQbEO2YpWu0m44Ewr-TyifTw1DGTK8CetOvESqyA6-M4YyZqyuKFP7-NeztNa61PORTXYPq8mNd5Z_08Gpii_PuRqIfXIl0WB3NkrV4qrR3rO4no6xfPvBOt0KlvWI5goDMF7HV9-vhtazBnF_1jlr2XVIzGjVyAhTMo-PQEok56GAwQAAAAHbGwTmAA", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Configurations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼️ Image URLs (Can be customized)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START_IMG_URL = os.getenv("START_IMG_URL", "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
STATS_IMG_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
STREAM_IMG_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/ea393ad4ce0eed46d32c8-b287bce17388905e79.jpg"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 User & Bot State Stores
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏳ Time Conversion Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Validate Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ✅ CONFIG LOADED SUCCESSFULLY | Designed By @WTF_WhyMeeh
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
