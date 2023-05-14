import asyncio
import re
import urllib
from pyrogram import Client, filters, idle
from config import *
from uvloop import install
import aiohttp
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import aiofiles
from contextlib import closing, suppress
from pyrogram.types import Message, MessageEntity
from string import ascii_letters, ascii_uppercase, digits
from base64 import standard_b64encode, standard_b64decode
app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )
app.start()

loop = asyncio.get_event_loop()

@app.on_message(filters.private & filters.regex("http|https"))
async def Bitly(bot, cmd: Message):
  URL = cmd.text
  api_url = f"http://ouo.press/api/jezWr0hG?s={URL}"
  opts = FirefoxOptions()
  opts.add_argument("--headless")
  browser = webdriver.Firefox(options=opts)
  result = browser.get(api_url)
  nyaa_text = result 
  fuktext = "`" + nyaa_text + "`"
  await cmd.reply_text(nyaa_text) 
    
async def start_bot():
  print("==================================")
  print("[INFO]: AutoAnimeBot Started Bot Successfully")
  print("==========JOIN @Latest_ongoing_airing_animes=========")
  
  await idle()
  print("[INFO]: BOT STOPPED")
  await app.stop()  
  for task in asyncio.all_tasks():
    task.cancel()

if __name__ == "__main__":
  install()
  with closing(loop):
    with suppress(asyncio.exceptions.CancelledError):
      loop.run_until_complete(start_bot())
      loop.run_until_complete(asyncio.sleep(3.0))
