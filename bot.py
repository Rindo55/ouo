import asyncio
import re
import json
import urllib
from pyrogram import Client, filters, idle
from config import *
from uvloop import install
import aiohttp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import undetected_chromedriver as uc
from seleniumbase import Driver
import time
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
    api_url = f"http://ouo.io/qs/jezWr0hG?s={bok}"
    driver = Driver(uc=True)
    
    result = driver.uc_open_with_reconnect(api_url)
    
    print(driver.current_url)
    print(driver.find_element(By.XPATH, "/html/body").text)
    element = driver.find_element_by_tag_name('body') 
    nai_text = element.text
    
    print(nai_text)
    da_url = "https://da.gd/"
    url = nai_text
    shorten_url = f"{da_url}shorten"
    response = scraper.post(shorten_url, params={"url": url})
    nyaa_text = response.text.strip()
    await cmd.reply_text(nyaa_text)
    
async def start_bot():
  print("==================================")
  print("[INFO]: ouo Started Bot Successfully")
  print("==========Visit ajax.to========")
  
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
