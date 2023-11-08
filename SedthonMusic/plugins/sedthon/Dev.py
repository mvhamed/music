import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from SedthonMusic import app, Telegram
import random
@app.on_message(
    command(["سيدثون","سورس","السورس","سورس سيدثون", "السيدثون"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/45a08298c226a89563e4d.mp4",
        caption=f"""
 [𝗦𝞝𝗗𝙏𝙃𝙊𝙉 𝗨ꜱᴇʀʙᴏᴛ](https://t.me/veebvw)
 —————————————
 [اެݪ تِــاެࢪيٰــخَ ¦ BiLaL](https://t.me/NUNUU)
 
 [𓏺𝙂𝙍𝙊𝙐𝙋 𝙃𝞝𝙇𝙋](https://t.me/TIPTHON_help)
  
 [⍟𓏺𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝗦𝞝𝗗𝙏𝙃𝙊𝙉 𝗨ꜱᴇʀʙᴏᴛ](https://t.me/veevvw)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اެݪ تِــاެࢪيٰــخَ ¦ BiLaL", url=f"https://t.me/nunuu"), 
                ],[
                    InlineKeyboardButton(
                        "𝗦𝞝𝗗𝙏𝙃𝙊𝙉 𝗨ꜱᴇʀʙᴏᴛ", url=f"t.me/veevvw"),
                ],

            ]

        ),

    )

@app.on_message(command([f"غنيلي", "غني", "غ", "{BOT_USERNAME} غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/iV_P_Nl/{rl}"
    await client.send_voice(message.chat.id,url,caption="`🔥 ¦ تـم اختيـار الاغـنـية لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="`💕 ¦ تـم اختيـار الصوره لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        
