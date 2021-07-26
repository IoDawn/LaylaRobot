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
def admin_callback(update, context):
    query = update.callback_query
    if query.data == "admin_":
        query.message.edit_text(
            text="""📕 *Aᴅᴍɪɴ-Mᴇɴᴜ*
                 \n""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Staff", callback_data="staf_"),
                        InlineKeyboardButton(text="Power", callback_data="power_"),
                    ],
                    [
                        InlineKeyboardButton(text="Approve", callback_data="izin_"),
                        InlineKeyboardButton(text="Connect", callback_data="konek_"),
                    ],
                    [
                        InlineKeyboardButton(text="Reports", callback_data="lapor_"),
                        InlineKeyboardButton(text="Warns", callback_data="warned_"),
                    ],
                    [   
                        InlineKeyboardButton(text="➩", callback_data="plugin_")],
                ]
            ),
        )


@run_async
def staf_callback(update, context):
    query = update.callback_query
    if query.data == "staf_":
        query.message.edit_text(
            text="""Commands for *Staff*
• /staff: cek daftar admin
                 \n*Khusus Admin:*
• /pin: sematkan pesan
• /unpin: lepas semat
• /invitelink: cek tautan grup
• /promote: promosikan user
• /demote: turunkan user
• /title: atur title admin
• /reload: refresh daftar admin
• /antispam (on/off)
• /setgtitle: atur nama grup
• /setgpic: atur profil grup
• /delgpic: hapus profil grup
• /setsticker: atur stiker grup
• /setdescription: atur desk grup
• /zombies: cari akun mati
• /zombies clean: kick akun mati""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="admin_")]]
            ),
        )

@run_async
def power_callback(update, context):
    query = update.callback_query
    if query.data == "power_":
        query.message.edit_text(
            text="""Commands for *Power*
• /punchme: kick pengguna yg menggunakan perintah ini.
                 \n*Cmd of Banned:*
• /ban: ban user
• /unban: lepas ban user
• /punch: kick user
• /sban: ban user diam²
• /tban: ban user sampai waktu yg anda tentukan
                 \n*Cmd of Mute:*
• /mute: bisukan pengguna
• /unmute: bunyikan pengguna
• /tmute: bisukan user sampai waktu yg anda tentukan""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="admin_")]]
            ),
        )


@run_async
def izin_callback(update, context):
    query = update.callback_query
    if query.data == "izin_":
        query.message.edit_text(
            text="""Commands for *Approve*
                 \n*Perintah admin:*
• /approval: periksa status persetujuan pengguna digrup.
• /approve: bebaskan member dari hukuman blacklist, lock, dll.
• /unapprove: hapus daftar pengguna yang dibebaskan.
• /approved: daftar semua pengguna yang dibebaskan.
• /unapproveall: Batalkan pembebasan SEMUA pengguna.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="admin_")]]
            ),
        )


@run_async
def konek_callback(update, context):
    query = update.callback_query
    if query.data == "konek_":
        query.message.edit_text(
            text="""Command of *Connect*
• /connect: hubungkan grup ke bot untuk perintah jarak jauh
• /connection: daftar grup yg terkoneksi dengan bot
• /disconnect: putuskan koneksi grup yg tersambung
• /helpconnect: list cmd yang tersedia dan dapat digunakan dari jarak jauh
• /allowconnect (on/off): izinkan member untuk koneksi dgn bot""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="admin_")]]
            ),
        )


@run_async
def lapor_callback(update, context):
    query = update.callback_query
    if query.data == "lapor_":
        query.message.edit_text(
            text="""Commands for *Reports*
• /report (alasan): laporkan user
• @admin: reply chat untuk melaporkan pengguna ke admin
                 \n*Khusus Admin:*
• /reports (on/off): mengubah pengaturan laporan grup""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="admin_")]]
            ),
        )


@run_async
def warned_callback(update, context):
    query = update.callback_query
    if query.data == "warned_":
        query.message.edit_text(
            text="""Commands for *Warns*
• /warns: cek warn user
• /warnlist: cek daftar kata warn
                 \n*Khusus Admin:*
• /warn: warn pengguna
• /dwarn: warn & hapus chatnya
• /resetwarn: hapus warn
• /addwarn: atur kata warn
• /nowarn: stop filter warn
• /warnlimit: atur batas warn
• /strongwarn (on/off): kick user yg melebihi batas warn""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="➥", callback_data="admin_")]]
            ),
        )

    plugin_about_callback = CallbackQueryHandler(plugin_about_callback, pattern=r"plugin_")
    admin_callback_handler = CallbackQueryHandler(admin_callback, pattern=r"admin_")
    staf_callback_handler = CallbackQueryHandler(staf_callback, pattern=r"staf_")
    power_callback_handler = CallbackQueryHandler(power_callback, pattern=r"power_")
    izin_callback_handler = CallbackQueryHandler(izin_callback, pattern=r"izin_")
    konek_callback_handler = CallbackQueryHandler(konek_callback, pattern=r"konek_")
    lapor_callback_handler = CallbackQueryHandler(lapor_callback, pattern=r"lapor_")
    warned_callback_handler = CallbackQueryHandler(warned_callback, pattern=r"warned_")

    dispatcher.add_handler(plugin_callback_handler)
    dispatcher.add_handler(admin_callback_handler)
    dispatcher.add_handler(staf_callback_handler)
    dispatcher.add_handler(power_callback_handler)
    dispatcher.add_handler(izin_callback_handler)
    dispatcher.add_handler(konek_callback_handler)
    dispatcher.add_handler(lapor_callback_handler)
    dispatcher.add_handler(warned_callback_handler)
