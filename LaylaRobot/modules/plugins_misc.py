from LaylaRobot.modules import ALL_MODULES
from LaylaRobot.modules.plugins_admin import plugin_about_callback
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
def miks_callback(update, context):
    query = update.callback_query
    if query.data == "miks_":
        query.message.edit_text(
            text="""📙 *Mɪsᴄ-Mᴇɴᴜ*
                 \n""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Math", callback_data="gmath_"),
                    ],
                    [
                        InlineKeyboardButton(text="Extra", callback_data="gextra_"),
                        InlineKeyboardButton(text="Other", callback_data="gother_"),
                    ],
                    [   
                        InlineKeyboardButton(text="➩", callback_data="plugin_")],
                ]
            ),
        )


@run_async
def gmath_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "gmath_":
        query.message.edit_text(
            text="""Commands for *Math*
• /math: hitungan
• /factor: faktor
• /derive: derive
• /integrate: integrasi
• /zeroes: cari 0's 
• /tangent: cari tangent
• /area: area di bawah kurva
• /cos: cosinus
• /sin: sinus
• /tan: tangent 
• /arccos: inverse Cosine
• /arcsin: inverse Sine
• /arctan: inverse Tangent
• /abs: nilai mutlak
• /log: logarithma""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="miks_")]]
            ),
        )


@run_async
def gextra_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "gextra_":
        query.message.edit_text(
            text="""Commands for *Extra*
                 \n*Fake Info*
• /fakegen: bin palsu
• /picgen: gen palsu
                 \n*Converts*
• /encrypt: baca enskripisi teks
• /decrypt: buat teks enskripisi
• /zip: kompres file ke zip
• /unzip: dekompres file ke zip""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="miks_")]]
            ),
        )


@run_async
def gother_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "gother_":
        query.message.edit_text(
            text="""Commands for *Other*
• /markdownhelp: cek pemformatan markdown
• /paste: paste teks ke nekobin
• /react: reaksi acak
• /tts: teks ke suara
• /ud: kamus urban
• /wiki: wikipedia
• /wall: cari wallpaper
• /cs: cricket info
• /cash: konversi mata uang""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="miks_")]]
            ),
        )

    plugin_about_callback = CallbackQueryHandler(plugin_about_callback, pattern=r"plugin_")
    miks_callback_handler = CallbackQueryHandler(miks_callback, pattern=r"miks_")
    gmath_callback_handler = CallbackQueryHandler(gmath_callback, pattern=r"gmath_")
    gextra_callback_handler = CallbackQueryHandler(gextra_callback, pattern=r"gextra_")
    gother_callback_handler = CallbackQueryHandler(gother_callback, pattern=r"gother_")

    dispatcher.add_handler(plugin_callback_handler)
    dispatcher.add_handler(miks_callback_handler)
    dispatcher.add_handler(gmath_callback_handler)
    dispatcher.add_handler(gextra_callback_handler)
    dispatcher.add_handler(gother_callback_handler)
