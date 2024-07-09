import logging
from sqlalchemy.orm import Session
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.dispatcher.router import Router
from DB.create import addObject
from DB.deleter import delObj
from DB.models import User
from config import *

logging.basicConfig(level=logging.INFO)

async def cmd_start(message: types.Message):
    """
    Обработчик команды /start. Добавляет нового пользователя в базу данных или сообщает, что пользователь уже зарегистрирован.
    Если пользователь является администратором, ему отправляется кастомная клавиатура.
    
    Args:
        message (types.Message): Сообщение с командой /start.
    """
    session = Session(engine)
    user = session.query(User).get(message.from_user.id)
    
    if not user:
        user = User(
            TG_ID=message.from_user.id,
            UserName=message.from_user.first_name
        )
        addObject(user)
        await message.answer(f'Пользователь:\n{message.from_user.first_name} с ID:{message.from_user.id}\ндобавлен\nchat_id {message.chat.id}')
    else:
        await message.answer(f'Пользователь:\н{message.from_user.first_name} с ID:{message.from_user.id}\нбыл зарегистрирован')

    if isAdmin(message.from_user.id):
        admin_keyboard = ReplyKeyboardMarkup(keyboard=[[
            KeyboardButton(text='Пользователи')
        ]], resize_keyboard=True)
        await message.answer("Привет, администратор!", reply_markup=admin_keyboard)

async def cmd_del(message: types.Message):
    """
    Обработчик команды /del. Удаляет пользователя из базы данных, если команда выполнена администратором.
    
    Args:
        message (types.Message): Сообщение с командой /del.
    """
    if isAdmin(message.from_user.id):
        try:
            delObj(message.from_user.id, User)
            await message.answer(f'Пользователь {message.from_user.id} удалён')
        except:
            await message.answer('Данного пользователя не существует')

async def on_startup(bot: Bot):
    await bot.send_message(chat_id=352923545, text="Бот успешно запущен!")

def register_handlers(router: Router):
    """
    Регистрирует обработчики команд в роутере.
    
    Args:
        router (Router): Роутер для регистрации обработчиков.
    """
    router.message.register(cmd_start, Command(commands=["start"]))
    router.message.register(cmd_del, Command(commands=["del"]))
