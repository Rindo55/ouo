import asyncio
import re
import json
import urllib
from pyrogram import Client, filters, idle
from config import *
from uvloop import install
import aiohttp
import requests
import undetected_chromedriver as uc
from selenium import webdriver
import cloudscraper
import aiofiles
from contextlib import closing, suppress
from pyrogram.types import Message, MessageEntity
from string import ascii_letters, ascii_uppercase, digits
from base64 import standard_b64encode, standard_b64decode
from ouo.api import Ouo
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
    bok = str(cmd.text)
    api_url = f"http://ouo.io/api/jezWr0hG?s={bok}"
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.binary_location = "/usr/bin/google-chrome"
    options.browser_executable_path = "/usr/bin/google-chrome" 
    driver = uc.Chrome(options=options)
    result = driver.get(api_url)
    nai_text = result.text
    
    print(nai_text)
    da_url = "https://da.gd/"
    url = nai_text
    shorten_url = f"{da_url}shorten"
    response = scraper.post(shorten_url, params={"url": url})
    nyaa_text = response.text.strip()
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
