import html
import json
import random
from datetime import datetime
from typing import Optional, List
import time
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
                                                                   
from kaga import dispatcher
from kaga.modules.disable import DisableAbleCommandHandler
from kaga.modules.helper_funcs.extraction import extract_user
from kaga.modules.helper_funcs.filters import CustomFilters
from kaga.modules.helper_funcs.alternate import typing_action

from geopy.geocoders import Nominatim
from telegram import Location


GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"



def gps(update, context):
    args = context.args
    message = update.effective_message
    if len(args) == 0:
        update.effective_message.reply_text("That was a funny joke, but no really, put in a location")
    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = " ".join(args)
        geoloc = geolocator.geocode(location)  
        chat_id = update.effective_chat.id
        lon = geoloc.longitude
        lat = geoloc.latitude
        the_loc = Location(lon, lat) 
        gm = "https://www.google.com/maps/search/{},{}".format(lat,lon)
        bot.send_location(chat_id, location=the_loc)
        update.message.reply_text("Open with: [Google Maps]({})".format(gm), parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
    except AttributeError:
        update.message.reply_text("I can't find that")


__help__ = """
- /gps: <location> Get gps location..
"""

__mod_name__ = "Gps"

GPS_HANDLER = DisableAbleCommandHandler("gps", gps, pass_args=True)

dispatcher.add_handler(GPS_HANDLER)