from telegram import (
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext
from LaylaRobot.modules.language import gs

def fmt_md_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        gs(update.effective_chat.id, "md_help"),
        parse_mode=ParseMode.HTML,
    )


def fmt_filling_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        gs(update.effective_chat.id, "filling_help"),
        parse_mode=ParseMode.HTML,
    )


__mod_name__ = 'Formatting'

def get_help(chat):
    return [gs(chat, "formt_help_bse"),
    [
        InlineKeyboardButton(text="Markdown", callback_data="md_help"),
        InlineKeyboardButton(text="Filling", callback_data="filling_help")
    ]
]
