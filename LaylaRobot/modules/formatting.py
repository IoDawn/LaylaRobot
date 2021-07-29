from LaylaRobot.modules import ALL_MODULES
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import TelegramError
from telegram.ext.dispatcher import run_async
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)


__mod_name__ = "Formatting"

__help__ = """
Hei.. nama saya Roso
Test formatting
"""

buttons = [
    [
        InlineKeyboardButton(
            text="➕ Add to your Group ➕", url="t.me/RosoManage2_bot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(
            text="ℹ️ About", url="t.me/RosoManage2_bot"),
        InlineKeyboardButton(
            text="Plugins ⏹", url="t.me/RosoManage2_bot"),
    ],
    [  
        InlineKeyboardButton(text="🔘 More-Bot 🔘", url="t.me/RosoManage2_bot"
    ),
    ],
]
