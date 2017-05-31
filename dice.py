#!/usr/bin/env python3

import logging

from telegram.ext import Updater, CommandHandler, InlineQueryHandler


def help(bot, update):
    update.message.reply_text('Hello World!')


def initialize(bot, update, token):
    logging.basicConfig(level=logging.DEBUG)

    updater = Updater(token=token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('help', help))

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    updater.start_polling()
    updater.idle()
