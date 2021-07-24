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
def admin_callback(update, context):
    query = update.callback_query
    if query.data == "admin_":
        query.message.edit_text(
            text="""Here are some bots that can help you:
 ✪ Shield*:* bot for protect your group from NSFW senders and Spam.
 ✪ Manage*:* similar to this bot with Indonesian language plugins.
 ✪ Music*:* bot to play music in your group chat.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Open", callback_data="admin_back")]]
            ),
        )
    elif query.data == "admin_back":
        query.message.edit_text(
                PM_START_TEXT,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )


    admin_callback_handler = CallbackQueryHandler(admin_callback, pattern=r"admin_")

    dispatcher.add_handler(admin_callback_handler)
