# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
# Owner https://t.me/ll_BAD_MUNDA_ll

import json
import os

from BADMUSIC.core.bot import BADBOT
from BADMUSIC.core.dir import dirr
from BADMUSIC.core.git import git
from BADMUSIC.core.userbot import Userbot
from BADMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

# Bot Client

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

app = BADBOT()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}

TOKEN = {
    "access_token": "ya29.a0AeDClZCLlhlJYBkVP4wZ2ytvOrenU-LzKVwks88uqRBddHNQjD_3ULCYaXVdDtzo1OGh392nz7lTMen0QAfNzWhhIa9vTbu3Y_m-lItoT4UvN7rQosr2-PLl_ZAq1tAW9yR0MnKccfvxY6GMvurmUOHakgSE-mKNULOcxjw82CjO75Ed9a6caCgYKARYSARISFQHGX2MiHjDU76ALyeiOP3mfqtmR3Q0187",
    "expires": 1729991307.801946,
    "token_type": "Bearer",
    "refresh_token": "1//05vYI0c8OP0b4CgYIARAAGAUSNwF-L9IrJvP8EzLj-4wkJD-hYD9y1fXRNSGS9CjEQ1YwRxFw1OjatSgXsGooDbs5QcqAPOs3TvM"
    }
# Convert TOKEN dictionary to a JSON string
os.environ["TOKEN_DATA"] = json.dumps(TOKEN)
