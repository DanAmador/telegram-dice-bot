#!/usr/bin/env python3

import logging
import random, time
import re
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
import numpy

def start(bot, update):
    update.message.reply_text("""Returns a random value. To use this bot send and inline query with the following format:

@tdice_bot  #d#             where # represents a number.

For example 1d6 returns a random value from 1 to 6 or 2d20 returns 2 random values between 1 and 20""")


def random_number(limit, amount):
    return  random.sample(range(limit), amount)


def dice_roll(bot, update):
    query_string = update.inline_query.query
    logging.log(logging.DEBUG, time.clock())
    results = []
    if re.search("\d+[d]+\d", query_string) is not None:
        query = [int(i) for i in re.findall(r'\d+', query_string)]
        d_results = "Roll {} {}-faced die \n".format(query[0], query[1])
        result = random_number(query[1], query[0])
        for i in range(query[0]):
            d_results += "{}.- {} \n".format(i + 1, result[i])

        results.append(InlineQueryResultArticle(id=uuid4(), title="Roll {}   {}-faced die ".format(query[0], query[1]),
                                                input_message_content=InputTextMessageContent(d_results)))

    elif re.search("\d+[d]+[p]", query_string) is not None:
        query = [int(i) for i in re.findall(r'\d+', query_string)]

        d_results = "Roll {} percentage die \n".format(query[0])
        result = random_number(100, query[0])

        for i in range(query[0]):
            d_results += "{}.- {}% \n".format(i + 1, result[i])
        results.append(InlineQueryResultArticle(id=uuid4(), title="Roll {} percentage die ".format(query[0]),
                                                input_message_content=InputTextMessageContent(d_results)))
    else:
        results.append(InlineQueryResultArticle(id=uuid4(), title="Please use the correct nomenclature",
                                                input_message_content=InputTextMessageContent(
                                                        "{} is not a correct nomenclature, for more info visit @tdice_bot".format(query_string))))
    update.inline_query.answer(results)


cryptogen = random.SystemRandom()


def initialize(token):
    logging.basicConfig(level=logging.DEBUG)

    updater = Updater(token=token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(InlineQueryHandler(dice_roll))
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    updater.start_polling()
    updater.idle()
