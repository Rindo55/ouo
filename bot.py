import asyncio
import re
import json
import urllib
from pyrogram import Client, filters, idle
from config import *
from uvloop import install
import aiohttp
import requests
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

@app.on_message(filters.private)
async def Bitly(bot, cmd: Message):
  URL = str(cmd.text)
  api_url = f"https://api.safone.me/weather?city=Bangalore"
  result = requests.post(api_url).json()
  nai_text = result['description']
  await cmd.reply_text(nai_text)  
    
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
