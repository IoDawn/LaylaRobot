import html
import random
import LaylaRobot.modules.truth_and_dare_string as truth_and_dare_string
from LaylaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from LaylaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

@run_async
def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))

@run_async
def quote(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.QUOTE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
TRUTH_REGEX_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"^(?i)truth(.*)$"), truth, friendly="truth"
)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
QUOTE_HANDLER = DisableAbleCommandHandler("quote", quote)


dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(TRUTH_REGEX_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(QUOTE_HANDLER)

