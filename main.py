import asyncio 
import logging
from aiogram import Bot, Dispatcher

from my_config import config_bot
from app.handlers import router

async def main():
    logging.basicConfig(level = logging.INFO, filename = "py_logbot.log", filemode = "w")
    bot = Bot(token=config_bot.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("The bot is shut down")

