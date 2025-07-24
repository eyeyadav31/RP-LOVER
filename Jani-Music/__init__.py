from Jani-Music.core.bot import Istkhar
from Jani-Music.core.dir import dirr
from Jani-Music.core.git import git
from Jani-Music.core.userbot import Userbot
from Jani-Music.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Istkhar()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
