import asyncio
from aiogram import Dispatcher
from logger import logger
from bot import get_bot

from handlers import basic_handlers
from handlers import game_handler
    
async def main():
    logger.info('Started bot')

    bot = get_bot()
    dp = Dispatcher()

    dp.include_router(basic_handlers.router)
    dp.include_router(game_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())