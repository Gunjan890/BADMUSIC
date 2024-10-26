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

YOUTUBE = {
    "access_token": "ya29.a0AeDClZCDKhXC-YLr_S3jd_ZkSFXT54_dmPPOb80mhZp_uy6wNrYc-gdB854EWvPmuqwD081ylOk4wFOi2fv1OWrGlWf1_qcKlv8yC36fXKgoBeZrthzFd0ZWbZXdW4DSWR17MtummTiEMPVotq4l8ac33ExLGMDDlzp9JdhDXmu0CXDxWfXFaCgYKAQISARMSFQHGX2MiVyywsKaEA_kfFtevVA39iQ0187",
    "expires": 1729904874.609338,
    "refresh_token": "1//05sOjboIry-okCgYIARAAGAUSNwF-L9IrgZfECyUbFqLVlbW7zt93dgucdf-uDnpKgH0GD7wQypX9ZBikWtNNOm28nGbRmjBIsUo",
    "token_type": "Bearer",
}

os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
