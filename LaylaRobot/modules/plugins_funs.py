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
def fan_callback(update, context):
    query = update.callback_query
    if query.data == "fan_":
        query.message.edit_text(
            text="""📘 *Fᴜɴs-Mᴇɴᴜ*
                 \n""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Anime", callback_data="fanime_"),
                    ],
                    [
                        InlineKeyboardButton(text="Couple", callback_data="fcouple_"),
                        InlineKeyboardButton(text="Game", callback_data="fgame_"),
                    ],
                    [
                        InlineKeyboardButton(text="Logo", callback_data="flogo_"),
                        InlineKeyboardButton(text="Meme", callback_data="fmeme_"),
                    ],
                    [
                        InlineKeyboardButton(text="Music", callback_data="fmusic_"),
                        InlineKeyboardButton(text="Sticker", callback_data="fstiker_"),
                    ],
                    [   
                        InlineKeyboardButton(text="➩", callback_data="plugin_")],
                ]
            ),
        )


@run_async
def fanime_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fanime_":
        query.message.edit_text(
            text="""Commands for *Anime*
• /character: cek info karakter
• /manga: cek info manga
• /user: cek info pengguna
• /upcoming: daftar anime baru dimusim yg akan datang
•  /kaizoku: cari anime di animekaizoku.com
• /airing: info penayangan anime""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="fan_")]]
            ),
        )


@run_async
def fcouple_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fcouple_":
        query.message.edit_text(
            text="""Command for *Couple*
• /shipping: jodohkan orang""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="fan_")]]
            ),
        )


@run_async
def fgame_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fgame_":
        query.message.edit_text(
            text="""Commands for *Game*
                 \n*Play Game With Emojis:*
 • /dice 🎲
 • /ball 🏀
 • /dart 🎯
*Play Game With Animations:*
 • /hack 🧑‍💻
 • /love ❣
 • /kill 🏹
*Play Game With Questions:*
 • /truth: pertanyaan kejujuran
 • /dare: pertanyaan tantangan""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="fan_")]]
            ),
        )


@run_async
def flogo_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "flogo_":
        query.message.edit_text(
            text="""Commands for *Logo*
• /logo (teks): buat teks logo
• /wlogo (teks): sama, tetapi dengan font yang berbeda""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="fan_")]]
            ),
        )


@run_async
def fmeme_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fmeme_":
        query.message.edit_text(
            text="""Commands for *Meme*
• /runs: lari ada wibu
• /slap: tampar pengguna
• /shrug: angkat bahu
• /table: dapatkan flip/unflip
• /decide: jawaban acak
• /toss: lempar koin
• /bluetext: cek sendiri
• /roll: lempar dadu
• /rlg: emot teks
• /shout (teks): cobain aja
• /weebify: teks weebified
• /pat: menepuk pengguna
• /8ball: prediksi warna
• /insult: menyindir anda""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="fan_")]]
            ),
        )


@run_async
def fmusic_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fmusic_":
        query.message.edit_text(
            text="""Commands for *Music*
• /song: search lagu diyt
• /video: search video yt
• /deezer: cari lagu di deezer
• /lyrics: cari lirik lagu
• /glyrics: cari judul beserta nama artis dari lirik lagu""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="fan_")]]
            ),
        )


@run_async
def fstiker_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fstiker_":
        query.message.edit_text(
            text="""Commands for *Sticker*
• /stickerid: cek id stiker
• /getsticker: stiker ke foto
• /kang: colong stiker
• /stickers: cari nama stiker""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="fan_")]]
            ),
        )
