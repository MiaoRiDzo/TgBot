import asyncio
import logging
from config import *
from DB.create import *
from DB.model import User
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user = User(
        TG_ID = message.from_user.id,
        UserName = message.from_user.first_name
    )
    addObject(user)
    await message.answer(f'Пользователь {user.UserName} с ID {user.TG_ID} добавлен')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())