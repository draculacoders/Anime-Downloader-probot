import os
import config
import logging
from telethon import TelegramClient

from pyrogram import *
from pyrogram.handlers import *
from Anime_Downloader_Probot.anime_search import anime_search
from Anime_Downloader_Probot.start_message import start_message
from Anime_Downloader_Probot.dev_info import dev_info
from Anime_Downloader_Probot.genres import genres
from Anime_Downloader_Probot.genre_results import genre_results
from Anime_Downloader_Probot.get_anime_details import anime_details
from Anime_Downloader_Probot.inline_search import inline_search
from Anime_Downloader_Probot.get_episodes_index import get_epIndex
from Anime_Downloader_Probot.get_episode_link import get_ep_link
from Anime_Downloader_Probot.instructions import instructions
from Anime_Downloader_Probot.airing import airing_eps
from Anime_Downloader_Probot.recently import recently_eps
from Anime_Downloader_Probot.inline_search_results import anime_inline_details
from Anime_Downloader_Probot.get_ep_numbers import get_ep


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

pgram = TelegramClient('bot', API_ID, API_HASH).start(bot_token=TG_BOT_TOKEN)

# Adding all functions to Handlers in main() function
def main():
    pgram.add_handler(MessageHandler(anime_search, filters.regex(r'search')), group=1)
    pgram.add_handler(MessageHandler(start_message, filters.command('start')), group=2)
    pgram.add_handler(MessageHandler(dev_info, filters.command('info')), group=3)
    pgram.add_handler(MessageHandler(genres, filters.command('genres')), group=4)
    pgram.add_handler(InlineQueryHandler(inline_search), group=6)
    pgram.add_handler(MessageHandler(airing_eps, filters.command("airing")), group=7)
    pgram.add_handler(CallbackQueryHandler(anime_details, filters.regex('dt_*')), group=8)
    pgram.add_handler(CallbackQueryHandler(get_epIndex, filters.regex('dl_*')), group=9)
    pgram.add_handler(CallbackQueryHandler(get_ep_link, filters.regex('eps_*')), group=10)
    pgram.add_handler(CallbackQueryHandler(genre_results, filters.regex('genre/')), group=11)
    pgram.add_handler(CallbackQueryHandler(instructions, filters.regex('instructions')), group=12)
    pgram.add_handler(MessageHandler(anime_inline_details, filters.text), group=13)
    pgram.add_handler(CallbackQueryHandler(get_ep, filters.regex('eplink_*')), group=14)
    
    pgram.add_handler(MessageHandler(recently_eps, filters.command("recently")), group=15)

# Calling main method and handlers, polling state
if __name__ == '__main__':
    pgram.run(main())
