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


@run_async
def Other_about_callback(update, context):
    query = update.callback_query
    if query.data == "other_":
        query.message.edit_text(
            text="""Here are some bots that can help you:
 ✪ Shield*:* bot for protect your group from NSFW senders and Spam.
 ✪ Manage*:* similar to this bot with Indonesian language plugins.
 ✪ Music*:* bot to play music in your group chat.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Shield", url="t.me/SpamProtectionRobot"),
                        InlineKeyboardButton(text="Manage", url="t.me/RosoManage_bot"),
                        InlineKeyboardButton(text="Music", url="t.me/RosoMusic_bot"),
                    ],
                    [   
                        InlineKeyboardButton(text="⌂", callback_data="other_back")],
                ]
            ),
        )
    elif query.data == "other_back":
        query.message.edit_text(
                PM_START_TEXT,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )
