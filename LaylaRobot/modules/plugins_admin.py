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
            text=f"*Mᴏᴅᴜʟᴇs ᴏғ Rᴏsᴏ*"
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
            text="""Plugin menu of *Admin*
                 \n""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Staff", callback_data="staf_"),
                        InlineKeyboardButton(text="Power", callback_data="staf_"),
                    ],
                    [
                        InlineKeyboardButton(text="Approve", callback_data="admin_"),
                        InlineKeyboardButton(text="Connect", callback_data="tools_"),
                    ],
                    [
                        InlineKeyboardButton(text="Reports", callback_data="funs_"),
                        InlineKeyboardButton(text="Warns", callback_data="misc_"),
                    ],
                    [   
                        InlineKeyboardButton(text="back", callback_data="plugin_")],
                ]
            ),
        )


@run_async
def staf_callback(update, context):
    query = update.callback_query
    if query.data == "staf_":
        query.message.edit_text(
            text="""Here is the help for the *Staff* module:
                 \n❍ /staff: Cek daftar admin di grup anda
                 \n*Admins only:*
 ❍ /pin: Menyematkan pesan yang dibalas tanpa notif- tambahkan 'loud' atau 'notify' untuk memberikan notifikasi kepada anggota grup
 ❍ /unpin: Melepas pin pesan yang saat ini disematkan
 ❍ /invitelink: Dapatkan tautan grup
 ❍ /promote: Promote user
 ❍ /demote: Turunkan jabatan user
 ❍ /title <title>: Menetapkan judul khusus untuk admin yang dipromosikan bot
 ❍ /reload: Refresh daftar admin
 ❍ /antispam <on/off>: Akan mengaktifkan teknologi antispam kami atau melihat pengaturan Anda saat ini.
 ❍ /setgtitle <title>: Menetapkan judul obrolan baru di grup Anda.
 ❍ /setgpic: Balas ke file atau foto untuk mengatur foto profil grup!
 ❍ /delgpic: Sama seperti di atas tetapi untuk menghapus foto profil grup.
 ❍ /setsticker: Balas ke stiker untuk menjadikannya sebagai pack stiker grup!
 ❍ /setdescription <deskripsi>: Tetapkan deskripsi obrolan baru di grup.
 ❍ /zombies: Temukan semua akun mati di grup Anda.
 ❍ /zombies clean: Hapus semua akun mati dari grup Anda.""",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="back", callback_data="admin_")]]
            ),
        )


    plugin_about_callback = CallbackQueryHandler(plugin_about_callback, pattern=r"plugin_")
    admin_callback_handler = CallbackQueryHandler(admin_callback, pattern=r"admin_")
    staf_callback_handler = CallbackQueryHandler(staf_callback, pattern=r"staf_")

    dispatcher.add_handler(plugin_callback_handler)
    dispatcher.add_handler(admin_callback_handler)
    dispatcher.add_handler(staf_callback_handler)
