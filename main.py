import os
import logging
import logging.config

import yaml

from src.bot import Bot


if __name__ == '__main__':
    with open("logging.conf.yml") as config_file:
        # print(yaml.safe_load("logging.conf.yml"))
        logging.config.dictConfig(yaml.safe_load(config_file))
    logger = logging.getLogger("telegram-bot")
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise Exception("Need to provide telegram token to bot")
    new_bot = Bot(bot_token)
    new_bot.start_bot()
