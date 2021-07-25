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
def manage_callback(update, context):
    query = update.callback_query
    if query.data == "manage_":
        query.message.edit_text(
            text="""ㅤ*【Mᴀɴᴀɢᴇ-Mᴇɴᴜ】*
                 \n""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Blacklist", callback_data="kata_"),
                    ],
                    [
                        InlineKeyboardButton(text="Channel", callback_data="chanel_"),
                        InlineKeyboardButton(text="Control", callback_data="kontrol_"),
                    ],
                    [
                        InlineKeyboardButton(text="F-Subs", callback_data="fsub_"),
                        InlineKeyboardButton(text="Feds", callback_data="feder_"),
                    ],
                    [
                        InlineKeyboardButton(text="Locks", callback_data="lok_"),
                        InlineKeyboardButton(text="Night", callback_data="malam_"),
                    ],
                    [
                        InlineKeyboardButton(text="Rules", callback_data="atur_"),
                        InlineKeyboardButton(text="Wlcm", callback_data="wlcm_"),
                    ],
                    [   
                        InlineKeyboardButton(text="➩", callback_data="plugin_")],
                ]
            ),
        )


@run_async
def kata_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "kata_":
        query.message.edit_text(
            text="""Command of *Blacklist*
                 \n*Blacklist kata/teks:*
• /blacklist: cek kata terlarang
*Khusus Admin:*
• /addblacklist: atur kata terlarang
• /unblacklist: hapus kata terlarang
• /blacklistmode: atur hukuman untuk kata terlarang
                 \n*Blacklist stiker:*
• /blsticker: lihat stiker terlarang
*Khusus Admin:*
• /addblsticker: atur stiker terlarang
• /unblsticker: hapus stiker terlarang
• /blstickermode: atur hukuman stiker terlarang""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def chanel_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "chanel_":
        query.message.edit_text(
            text="""Commands for *Log Channel*
                 \n*Khusus Admin:*
• /logchannel: cek log tertaut
• /setlog: atur log channel
• /unsetlog: hapus log channel""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def kontrol_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "kontrol_":
        query.message.edit_text(
            text="""Commands for *Control*
                 \n*Blue-Cleaned*
 • /cleanblue (on/off): menghapus perintah setelah dikirim
 • /ignoreblue (kata): mencegah pembersihan otomatis perintah
 • /unignoreblue (kata): nonaktifkan pencegah pembersihan otomatis dari perintah
 • /listblue: daftar perintah yang saat ini masuk daftar putih
                 \n*AntiFlood*
• /flood: lihat pengaturan saat ini
• /setflood: mengaktifkan atau menonaktifkan pengendalian banjir
• /setfloodmode: tindakan yang dilakukan ketika pengguna telah melampaui batas flood.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def fsub_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fsub_":
        query.message.edit_text(
            text="""Commands for *Force Subs*
                 \n*Khusus Owner:*
• /fsub {channel username} - untuk mengaktifkan dan mengatur channel.
• /fsub: cek pengaturan saat ini.
• /fsub disable: nonaktifkan fsub
• /fsub clear: untuk melepas semua anggota yang dibisukan oleh saya.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def feder_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "lok_":
        query.message.edit_text(
            text="""Commands for *Federation*
• /fedownerhelp: help untuk owner federasi
• /fedadminhelp: help untuk admin federasi
• /feduserhelp: help untuk semua pengguna federasi""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def lok_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "lok_":
        query.message.edit_text(
            text="""Commands for *Locks*
• /locktypes: daftar semua kemungkinan tipe lock
                 \n*Khusus admin:*
• /lock (tipe): mengunci item dari jenis tertentu
• /unlock (tipe): Buka item lock dari jenis tertentu
• /locks: daftar lock saat ini""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def malam_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "malam_":
        query.message.edit_text(
            text="""Command for *Night Mode*
                 \n*Khusus admin:*
• /nightmode (on/off): tutup grup pada jam 12Am - 6Am""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def atur_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "atur_":
        query.message.edit_text(
            text="""Commands for *Rules*
• /rules: lihat rules grup
                 \n*Khusus Admin:*
• /setrules: atur rules grup
• /clearrules: hapus rules grup""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )


@run_async
def wlcm_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "wlcm_":
        query.message.edit_text(
            text="""Commands for *Welcome*
                 \n*Khusus Admin:*
• /welcome (on/off): mengaktifkan/menonaktifkan pesan selamat datang.
• /welcome: lihat pengaturan welcome saat ini
• /welcome noformat: cek pengaturan welcome saat ini tanpa format
• /goodbye: aktifkan pesan goodbye
• /setwelcome: custom pesan welcome
• /setgoodbye (teks): custom pesan goodbye
• /resetwelcome: reset ke pesan welcome default
• /resetgoodbye: reset ke pesan welcome default
• /cleanwelcome (on/off): hapus pesan welcome sebelumnya saat anggota baru bergabung
• /welcomemutehelp: memberikan informasi tentang penyambutan bisu
• /cleanservice (on/off): hapus pesan layanan 'anggota bergabung'
• /welcomehelp: cara pemformatan welcome""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="manage_")]]
            ),
        )

    plugin_about_callback = CallbackQueryHandler(plugin_about_callback, pattern=r"plugin_")
    manage_callback_handler = CallbackQueryHandler(manage_callback, pattern=r"manage_")
    kata_callback_handler = CallbackQueryHandler(kata_callback, pattern=r"kata_")
    chanel_callback_handler = CallbackQueryHandler(chanel_callback, pattern=r"chanel_")
    kontrol_callback_handler = CallbackQueryHandler(kontrol_callback, pattern=r"kontrol_")
    fsub_callback_handler = CallbackQueryHandler(fsub_callback, pattern=r"fsub_")
    feder_callback_handler = CallbackQueryHandler(feder_callback, pattern=r"feder_")
    lok_callback_handler = CallbackQueryHandler(lok_callback, pattern=r"lok_")
    malam_callback_handler = CallbackQueryHandler(malam_callback, pattern=r"malam_")
    atur_callback_handler = CallbackQueryHandler(atur_callback, pattern=r"atur_")
    wlcm_callback_handler = CallbackQueryHandler(wlcm_callback, pattern=r"wlcm_")

    dispatcher.add_handler(plugin_callback_handler)
    dispatcher.add_handler(manage_callback_handler)
    dispatcher.add_handler(kata_callback_handler)
    dispatcher.add_handler(chanel_callback_handler)
    dispatcher.add_handler(kontrol_callback_handler)
    dispatcher.add_handler(fsub_callback_handler)
    dispatcher.add_handler(feder_callback_handler)
    dispatcher.add_handler(lok_callback_handler)
    dispatcher.add_handler(malam_callback_handler)
    dispatcher.add_handler(atur_callback_handler)
    dispatcher.add_handler(wlcm_callback_handler)
