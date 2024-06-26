import asyncio
import logging
from config import *
from DB.create import *
from DB.deleter import *
from DB.models import User
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user = User(
        TG_ID = int(message.from_user.id),
        UserName = message.from_user.first_name
    )
    await message.answer(f'Пользователь {user.UserName} с ID {user.TG_ID} добавлен')
    addObject(user)

@dp.message(Command("del"))
async def cmd_del(message: types.Message):
    session = Session(engine)
    user = session.query(User).get(message.from_user.id)
    try:
        delObj(user)
        await message.answer(f'Пользователь {user.UserName} с ID {user.TG_ID} удален')
    except Exception as error:
        await message.answer(f'Ошибка:\n{error}')




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())