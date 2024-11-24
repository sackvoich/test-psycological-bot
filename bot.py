import logging
import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import register_handlers
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.middleware import FSMContextMiddleware


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=TOKEN)
    storage = MemoryStorage() # Объявляем storage здесь
    dp = Dispatcher(storage=storage) # Передаем storage в Dispatcher

    register_handlers(dp)

    logger.info("Starting bot")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
