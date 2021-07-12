#Truth and Dare Plugins
#dare plugins

import html
import random
import LaylaRobot.modules.truth_and_dare_string as truth_and_dare_string
from LaylaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from LaylaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


__mod_name__ = "🀄️Dare"
__help__ = """
🏷 `/dare` : untuk tantangan acak

Jika ingin req pertanyaan kirim ke @RosoOwner_bot
"""

DARE_HANDLER = DisableAbleCommandHandler("dare", dare)


dispatcher.add_handler(DARE_HANDLER)
