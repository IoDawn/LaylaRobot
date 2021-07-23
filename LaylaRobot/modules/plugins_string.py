import html

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.utils.helpers import escape_markdown


ADMIN = (
    f"Here is the help for the Admin module:",
    f"❍ /staff: Cek daftar admin di grup anda",
    f"\n*Admins only:*",
    f"❍ /pin: Menyematkan pesan yang dibalas tanpa notif- tambahkan 'loud' atau 'notify' untuk memberikan notifikasi kepada anggota grup",
    f"❍ /unpin: Melepas pin pesan yang saat ini disematkan",
    f"❍ /invitelink: Dapatkan tautan grup",
    f"❍ /promote: Promote user",
    f"❍ /demote: Turunkan jabatan user",
    f"❍ /title <title>: Menetapkan judul khusus untuk admin yang dipromosikan bot",
    f"❍ /reload: Refresh daftar admin",
    f"❍ /antispam <on/off>: Akan mengaktifkan teknologi antispam kami atau melihat pengaturan Anda saat ini.",
    f"❍ /setgtitle <title>: Menetapkan judul obrolan baru di grup Anda.",
    f"❍ /setgpic: Balas ke file atau foto untuk mengatur foto profil grup!",
    f"❍ /delgpic: Sama seperti di atas tetapi untuk menghapus foto profil grup.",
    f"❍ /setsticker: Balas ke stiker untuk menjadikannya sebagai pack stiker grup!",
    f"❍ /setdescription <deskripsi>: Tetapkan deskripsi obrolan baru di grup.",
    f"❍ /zombies: Temukan semua akun mati di grup Anda.",
    f"❍ /zombies clean: Hapus semua akun mati dari grup Anda.",
