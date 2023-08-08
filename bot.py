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

@app.on_message(filters.private & filters.command("sxs") & filters.regex("http|https"))
async def Bitly(bot, cmd: Message):
  fx = " ".join(message.command[1:])
  xam = str(fx)
  da_url = "https://da.gd/"
  resp = f"https://sxslink.com/api?api=555d814b547a16c08f5c7cf99ae9bbe8edd34696&url={xam}&format=text"
  fukshare = requests.get(resp)
  tshare = fukshare.text
  cshare = tshare
  xshare_url = f"{da_url}shorten"
  tgshare = requests.get(xshare_url, params={"url": cshare})
  teleshare = tgshare.text.strip() 
  await cmd.reply_text(f"`{teleshare}`")  

@app.on_message(filters.private & filters.command("tn") & filters.regex("http|https"))
async def Bitly(bot, cmd: Message):
  fit = " ".join(message.command[1:])
  xamx = str(fit)
  da_urlx = "https://da.gd/"
  respx = f"https://tnlinks.in/api?api=1458ad61946fd6f5b8a93161c9cfd94733813566&url={xamx}&format=text"
  fuksharex = requests.get(respx)
  tsharex = fuksharex.text
  csharex = tsharex
  xshare_urlx = f"{da_urlx}shorten"
  tgsharex = requests.get(xshare_urlx, params={"url": csharex})
  telesharex = tgsharex.text.strip() 
  await cmd.reply_text(f"`{telesharex}`")
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
