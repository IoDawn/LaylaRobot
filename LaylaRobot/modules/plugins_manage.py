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
def plugin_about_callback(update, context):
    query = update.callback_query
    if query.data == "plugin_":
        query.message.edit_text(
            text=f"*Hᴇʟᴘ ᴍᴇɴᴜ ᴏғ Rᴏsᴏ*"
            f"➛ Cmds: `228`"
            f"➛ Plugins: `59`",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="⚙ Manage", callback_data="manage_"),
                    ],
                    [
                        InlineKeyboardButton(text="🛃 Admin", callback_data="admin_"),
                        InlineKeyboardButton(text="🧰 Tools", callback_data="tools_"),
                    ],
                    [
                        InlineKeyboardButton(text="🎮  Funs", callback_data="funs_"),
                        InlineKeyboardButton(text="🗂 Misc", callback_data="misc_"),
                    ],
                    [
                        InlineKeyboardButton(text="≣", callback_data="help_back"),
                        InlineKeyboardButton(text="⌂", callback_data="plugin_back"),   
                        InlineKeyboardButton(text="✕", callback_data="tutup_")],
                ]
            ),
        )
    elif query.data == "plugin_back":
        query.message.edit_text(
                PM_START_TEXT,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
        )


@run_async
def manage_callback(update, context):
    query = update.callback_query
    if query.data == "manage_":
        query.message.edit_text(
            text="""*Mᴀɴᴀɢᴇ-Mᴇɴᴜ*
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
