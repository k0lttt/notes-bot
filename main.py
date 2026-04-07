import asyncio 
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from my_config import config_bot
from app.handlers import user
from app.admin import admin

from app.database.models import init_models

import redis.asyncio as aioredis

async def main():
    redis = await aioredis.from_url(f"redis://localhost:6379/0")
    logging.basicConfig(level = logging.INFO, filename = "py_logbot.log", filemode = "w")
    bot = Bot(token=config_bot.bot_token.get_secret_value())
    dp = Dispatcher(storage=RedisStorage(redis))
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_routers(user, admin)
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    
    await init_models()
    logging.info("Bot started up")

 
async def shutdown(dispatcher: Dispatcher):
    logging.info("Bot shutting down")   
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("The bot is shut down")

