from LaylaRobot.modules.helper_funcs.chat_status import user_admin
from LaylaRobot.modules.disable import DisableAbleCommandHandler
from LaylaRobot import dispatcher

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

MARKDOWN_HELP = f"""
Markdown is a very powerful formatting tool supported by telegram. {dispatcher.bot.first_name} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

• <code>_italic_</code>: wrapping text with '_' will produce italic text
• <code>*bold*</code>: wrapping text with '*' will produce bold text
• <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
• <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
<b>Example:</b><code>[test](example.com)</code>

• <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
<b>Example:</b> <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.

Keep in mind that your message <b>MUST</b> contain some text other than just a button!
"""


@run_async
@user_admin
def echo(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            args[1], parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    else:
        message.reply_text(
            args[1], quote=False, parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    message.delete()


def markdown_help_sender(update: Update):
    update.effective_message.reply_text(MARKDOWN_HELP, parse_mode=ParseMode.HTML)
    update.effective_message.reply_text(
        "Try forwarding the following message to me, and you'll see, and Use #test!"
    )
    update.effective_message.reply_text(
        "/save test This is a markdown test. _italics_, *bold*, code, "
        "[URL](example.com) [button](buttonurl:github.com) "
        "[button2](buttonurl://google.com:same)"
    )


@run_async
def markdown_help(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        update.effective_message.reply_text(
            "Contact me in pm",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Markdown help",
                            url=f"t.me/{context.bot.username}?start=markdownhelp",
                        )
                    ]
                ]
            ),
        )
        return
    markdown_help_sender(update)


__help__ = """
*Perintah yang tersedia:*
*Markdown:*
 ❍ /markdownhelp*:* ringkasan singkat tentang cara kerja penurunan harga di telegram - hanya dapat dipanggil dalam obrolan pribadi
*Paste:*
 ❍ /paste*:* Menyimpan konten yang dibalas ke `nekobin.com` dan membalas dengan url
*React:*
 ❍ /react*:* Bereaksi dengan reaksi acak 
*Text to Speach*:
 ❍ /tts*:* Ubah teks menjadi rekaman suara
Contoh: `/tts id|halo roso disini` 
(id: kode bhs Indonesia)
*Urban Dictonary:*
 ❍ /ud <word>*:* Ketik kata atau ekspresi yang ingin Anda cari gunakan
*Wikipedia:*
 ❍ /wiki <query>*:* wikipedia permintaan Anda
*Wallpapers:*
 ❍ /wall <query>*:* Dapatkan wallpaper dari`wall.alphacoders.com`
*live cricket score*
 ❍ /cs*:* Skor langsung terbaru dari cricket info
*Currency converter:* 
 ❍ /cash*:* Pengonversi mata uang
Contoh:
 `/cash 1 USD INR`  
      _OR_
 `/cash 1 usd inr`
Output: `1.0 USD = 75.505 INR`

*MATHS*
Memecahkan masalah matematika yang kompleks menggunakan https://newton.now.sh
❍ /math*:* Math `/math 2^2+2(2)`
❍ /factor*:* Factor `/factor x^2 + 2x`
❍ /derive*:* Derive `/derive x^2+2x`
❍ /integrate*:* Integrate `/integrate x^2+2x`
❍ /zeroes*:* Find 0's `/zeroes x^2+2x`
❍ /tangent*:* Find Tangent `/tangent 2lx^3`
❍ /area*:* Area Under Curve `/area 2:4lx^3`
❍ /cos*:* Cosine `/cos pi`
❍ /sin*:* Sine `/sin 0`
❍ /tan*:* Tangent `/tan 0`
❍ /arccos*:* Inverse Cosine `/arccos 1`
❍ /arcsin*:* Inverse Sine `/arcsin 0`
❍ /arctan*:* Inverse Tangent `/arctan 0`
❍ /abs*:* Absolute Value `/abs -1`
❍ /log*:* Logarithm `/log 2l8`

_Perlu di ingat_: Untuk menemukan garis singgung suatu fungsi pada nilai x tertentu, kirim permintaan sebagai c | f (x) di mana c adalah nilai x yang diberikan dan f (x) adalah ekspresi fungsi, pemisahnya vertikal bar '|'. Lihat tabel di atas untuk contoh permintaan.
Untuk mencari luas di bawah suatu fungsi, kirim permintaan sebagai c: d | f (x) di mana c adalah nilai x awal, d adalah nilai akhir x, dan f (x) adalah fungsi di mana Anda ingin kurva antara dua nilai x.
Untuk menghitung pecahan, masukkan ekspresi sebagai penyebut pembilang (di atas). Misalnya, untuk memproses 2/4 Anda harus mengirimkan ekspresi Anda sebagai 2 (di atas) 4. Ekspresi hasilnya akan dalam notasi matematika standar (1/2, 3/4).

💡`Baca dari atas`
"""

ECHO_HANDLER = DisableAbleCommandHandler("echo", echo, filters=Filters.group)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help)

dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)

__mod_name__ = "❐ Misc"
__command_list__ = ["id", "echo"]
__handlers__ = [
    ECHO_HANDLER,
    MD_HELP_HANDLER,
]
