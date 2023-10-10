import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from SedthonMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from SedthonMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait




@app.on_message(filters.text & filters.group)
async def reply_to_owner(client, message):
    if 'المالك' in message.text:
        chat_id = message.chat.id
        f = "administrators"
        async for member in client.iter_chat_members(chat_id, filter=f):
            if member.status == "creator":
                id = member.user.id
                m = await client.get_chat(id)
                if m.photo:
                    photo = await client.download_media(m.photo.big_file_id)
                    await message.reply_photo(photo, caption=f"🧞‍♂️ ¦𝙽𝙰𝙼𝙴 : {m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 : @{m.username}\n🎃 ¦𝙸𝙳 : {m.id}\n💌 ¦𝙱𝙸𝙾 : {m.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃: {message.chat.id}")
                    break
                else:
                    await message.reply(f"• {member.user.mention}")
                    break
   

   
@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""") 

        

array = []
@Client.on_message(filters.command(["@all", "تاك","all"], "") & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("**التاك قيد التشغيل الان .**")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("**عذرا عزيزي هذا الامر للادمن الجروب فقط .**")
    return
  await message.reply_text("**جاري بدأ المنشن ، لايقاف الامر اضغط /cancel .**")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("all","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.get_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ›"
       if i == 20:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@Client.on_message(filters.command(["/cancel", "ايقاف التاك"], ""))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("**عذرا عزيزي هذا الامر للادمن الجروب فقط .**")
    return
  if message.chat.id not in array:
     await message.reply("**المنشن متوقف بي الفعل .**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("**تم ايقاف المنشن عزيزي .**")
    return




