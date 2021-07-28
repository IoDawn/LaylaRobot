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
def alat_callback(update, context):
    query = update.callback_query
    if query.data == "alat_":
        query.message.edit_text(
            text="""📗 *Tᴏᴏʟs-Mᴇɴᴜ*
                 \n""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Backup", callback_data="rbackup_"),
                        InlineKeyboardButton(text="Disable", callback_data="rdisable_"),
                    ],
                    [
                        InlineKeyboardButton(text="Filter", callback_data="rfilter_"),
                        InlineKeyboardButton(text="Google", callback_data="rgoogle_"),
                    ],
                    [
                        InlineKeyboardButton(text="Info", callback_data="rinfo_"),
                        InlineKeyboardButton(text="Notes", callback_data="rnotes_"),
                    ],
                    [
                        InlineKeyboardButton(text="T-Graph", callback_data="rtgraph_"),
                        InlineKeyboardButton(text="Tagger", callback_data="rtagger_"),
                    ],
                    [   
                        InlineKeyboardButton(text="➩", callback_data="plugin_")],
                ]
            ),
        )


@run_async
def rbackup_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rbackup_":
        query.message.edit_text(
            text="""Commands for *Backup*
                 \n*Khusus owner*:
• /import: transfer data grup
• /export: ekspor data grup""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )


@run_async
def rdisable_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rdisable_":
        query.message.edit_text(
            text="""Commands for *Disable*
• /cmds: periksa status perintah yang dinonaktifkan saat ini
                 \n*Khusus admin:*
• /enable: aktifkan perintah
• /disable: nonaktifkan perintah 
• /enablemodul: aktifkan semua perintah dalam modul
• /disablemodule: nonaktifkan semua perintah dalam modul
• /listcmds: daftar perintah""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )


@run_async
def rfilter_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rfilter_":
        query.message.edit_text(
            text="""Commands for *Filter*
• /filters: list filter aktif
• /filter (keyword): atur filter
• /stop (keyword): stop filter
• /removeallfilters: hapus semua filter
• /markdownhelp: cek pemformatan""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )


@run_async
def rgoogle_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rgoogle_":
        query.message.edit_text(
            text="""Commands for *Google*
• /google (teks): searching
• /img (teks): search foto
• /app: search aplikasi
• /quote: kata-kata bijak
• /gps: search lokasi 
• /github: search github info
• /country: cek info negara
• /imdb: cek info film
• /reverse: search gambar dari media yang dibalas.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )


@run_async
def rinfo_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rinfo_":
        query.message.edit_text(
            text="""Commands for *Info*
• /afk: tandai diri anda off
• off: sama dengan afk
                 \n*ID*
• /id: cek id anda/grup
• /gifid: cek id dari gif
                 \n*Info untuk pribadi*
• /setme: atur info anda
• /me: cek info anda atau orang lain
*Info untuk orang lain*
• /bio: cek bio anda/orang lain
• /setbio: atur bio untuk orang lain""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )


@run_async
def rnotes_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rnotes_":
        query.message.edit_text(
            text="""Commands for *Notes*
• /get: dapatkan nama notes yg dipilih
• `#<notename>`: sama seperti diatas
• /notes: list semua notes
• /number: menarik catatan nomor itu dalam daftar
                 \n*Khusus admin:*
• /save: simpan notes
• /clear: hapus notes yg dipilih
• /removeallnotes: hapus daftar semua notes""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )


@run_async
def rtgraph_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rtgraph_":
        query.message.edit_text(
            text="""Commands for *Telegraph*
• /txt : upload teks ke telegraph
• /tm : upload media ke telegraph""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )


@run_async
def rtagger_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "rtagger_":
        query.message.edit_text(
            text="""Command for *Tagger*
• /tagall: tag anggota grup""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="alat_")]]
            ),
        )

    plugin_callback_handler = CallbackQueryHandler(plugin_about_callback, pattern=r"plugin_")
    alat_callback_handler = CallbackQueryHandler(alat_callback, pattern=r"alat_")
    rbackup_callback_handler = CallbackQueryHandler(rbackup_callback, pattern=r"rbackup_")
    rdisable_callback_handler = CallbackQueryHandler(rdisable_callback, pattern=r"rdisable_")
    rfilter_callback_handler = CallbackQueryHandler(rfilter_callback, pattern=r"rfilter_")
    rgoogle_callback_handler = CallbackQueryHandler(rgoogle_callback, pattern=r"rgoogle_")
    rinfo_callback_handler = CallbackQueryHandler(rinfo_callback, pattern=r"rinfo_")
    rnotes_callback_handler = CallbackQueryHandler(rnotes_callback, pattern=r"rnotes_")
    rtgraph_callback_handler = CallbackQueryHandler(rtgraph_callback, pattern=r"rtgraph_")
    rtagger_callback_handler = CallbackQueryHandler(rtagger_callback, pattern=r"rtagger_")

    dispatcher.add_handler(plugin_callback_handler)
    dispatcher.add_handler(alat_callback_handler)
    dispatcher.add_handler(rbackup_callback_handler)
    dispatcher.add_handler(rdisable_callback_handler)
    dispatcher.add_handler(rfilter_callback_handler)
    dispatcher.add_handler(rgoogle_callback_handler)
    dispatcher.add_handler(rinfo_callback_handler)
    dispatcher.add_handler(rnotes_callback_handler)
    dispatcher.add_handler(rtgraph_callback_handler)
    dispatcher.add_handler(rtagger_callback_handler)
