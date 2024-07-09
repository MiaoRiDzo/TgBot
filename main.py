import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import *
from Modules.mStart import on_startup, register_handlers
from aiogram.dispatcher.router import Router

logging.basicConfig(level=logging.INFO)

async def main():
    """
    Основная асинхронная функция для запуска бота.
    """

    # Вызов функции on_startup перед запуском поллинга
    await on_startup(bot)

    # Начало поллинга
    await dp.start_polling(bot)

if __name__ == "__main__":
    """
    Точка входа в программу. Запускает основную функцию main.
    """
    asyncio.run(main())
