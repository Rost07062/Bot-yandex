import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import common, training
import config


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.BOT_TOKEN)

    dp.include_router(common.router)
    dp.include_router(training.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
