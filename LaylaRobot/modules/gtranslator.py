from google_trans_new import LANGUAGES, google_translator
from telegram.ext import CommandHandler, CallbackContext
from telegram import (
    Message,
    Chat,
    User,
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from LaylaRobot import dispatcher
from LaylaRobot import pbot as kp
from pyrogram import filters
from pyrogram.types import Message
from LaylaRobot.modules.disable import DisableAbleCommandHandler


__help__ = """ 
Gunakan modul ini untuk menerjemahkan.
*Commands:*
• `/tl` (or `/tr`): reply ke pesan, untuk terjemahkan ke bahasa Inggris.
• `/tl <lang>`: terjemahkan ke <lang>
eg: `/tl id`: terjemahkan ke Indonesia .
• `/tl <source>//<dest>`: terjemahkan dari <source> ke <lang>.
eg: `/tl id//en`: menerjemahkan dari bahasa Indonesia ke bahasa Inggris.
• [Kode bahasa untuk terjemahan](https://telegra.ph/Lang-Codes-03-19-3)
"""


trans = Translator()


@kp.on_message(filters.command(["tl", "tr"]))
async def translate(_, message: Message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("Reply to a message to translate it!")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"<b>Translated from {source} to {dest}</b>:\n"
        f"<code>{translation.text}</code>"
    )

    await message.reply_text(reply, parse_mode="html")


__mod_name__ = "G-Trans"
__command_list__ = ["tr", "tl"]


