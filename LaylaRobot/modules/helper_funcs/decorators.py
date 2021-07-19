from LaylaRobot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, InlineQueryHandler
from telegram.ext.filters import BaseFilter
from LaylaRobot import dispatcher
from typing import Optional, Union, List


    def callbackquery(self, pattern: str = None, run_async: bool = True):
        def _callbackquery(func):
            self._dispatcher.add_handler(CallbackQueryHandler(pattern=pattern, callback=func, run_async=run_async))
            log.debug(f'[METACALLBACK] Loaded callbackquery handler with pattern {pattern} for function {func.__name__}')
            return func
        return _callbackquery


metacallback = MetaTelegramHandler(d).callbackquery
