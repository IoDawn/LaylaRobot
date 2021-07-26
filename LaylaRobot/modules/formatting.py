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


@run_async
def get_help(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "get_help":
        query.message.edit_text(
            text=f"*test format*"
            f"",
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
                        InlineKeyboardButton(text="⌂", callback_data="help_back")],
                ]
            ),
        )
