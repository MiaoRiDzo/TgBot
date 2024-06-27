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
    if(not Session(engine).query(User).get(message.from_user.id)):
        user = User(
            TG_ID = message.from_user.id,
            UserName = message.from_user.first_name
        )
        await message.answer(f'Пользователь:\n{message.from_user.first_name} с ID:{message.from_user.id}\nдобавлен')
        addObject(user)
    else:
        await message.answer(f'Пользователь:\n{message.from_user.first_name} с ID:{message.from_user.id}\nбыл зарегистрирован')

@dp.message(Command("del"))
async def cmd_del(message: types.Message):
    try:
        delObj(message.from_user.id, User)
        await message.answer(f'user {message.from_user.id} deleted')
    except:
        await message.answer(f'Данного пользователя не существет')




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())