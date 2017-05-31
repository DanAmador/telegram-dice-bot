#!/usr/bin/env python3

import logging
import random

from telegram.ext import Updater, CommandHandler, InlineQueryHandler


def start(bot, update):
    update.message.reply_text("""Returns a random value. To use this bot send and inline query with the following format:

@tdice_bot #d#             where # represents a number.

For example 1d6 returns a random value from 1 to 6 or 2d20 returns 2 random values between 1 and 20""")


def dice_roll(bot, update):
    query = [int(s) for s in update.inline_query.query.split() if s.isdigit()]
    results = []
    for i in range(query[0]):
        results.append(random.randrange(1, query[1]))

    update.inline_query.answer(results)


def initialize(token):
    logging.basicConfig(level=logging.DEBUG)

    updater = Updater(token=token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', help))
    dispatcher.add_handler(InlineQueryHandler(dice_roll, pattern="\d+[d]+\d"))
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    initialize()
