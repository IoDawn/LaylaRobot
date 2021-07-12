#Truth and Dare Plugins
#truth plugins

import html
import random
import LaylaRobot.modules.truth_and_dare_string
from LaylaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from LaylaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


__mod_name__ = "🎴Truth"
__help__ = """
🏷 `/truth` : untuk kejujuran acak

Jika ingin req pertanyaan kirim ke @RosoOwner_bot
"""

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)


dispatcher.add_handler(TRUTH_HANDLER)
