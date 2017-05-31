# -*- coding: utf-8 -*-
import redis
import os
import dice
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = dice.initialize(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
