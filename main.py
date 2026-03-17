import asyncio 
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from my_config import config_bot
from app.handlers import router

import redis.asyncio as aioredis

async def main():
    redis = await aioredis.from_url(f"redis://localhost:6379/0")
    logging.basicConfig(level = logging.INFO, filename = "py_logbot.log", filemode = "w")
    bot = Bot(token=config_bot.bot_token.get_secret_value())
    dp = Dispatcher(storage=RedisStorage(redis))
    dp.include_router(router)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("The bot is shut down")

