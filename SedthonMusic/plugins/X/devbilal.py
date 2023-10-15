import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from SedthonMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from SedthonMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
















@app.on_message(filters.command("المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001783620120, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي الكروب {message.chat.id}\n- يوزر الكروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- **ابشر ياعيوني ارسلت للمطور اشعار الكروي ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت علمود تشوف التحديثات** -› [• Source sedthon •](t.me/E9N99)""", disable_web_page_preview=True     
    )




@app.on_message(filters.regex("^رابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين ياحلو\n-› هذي روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )
