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
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

            update.effective_message.reply_text(
                f"test format",
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
