from DB.create import *
from DB.deleter import *
from DB.models import User
from Modules.mStart import register_handlers
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command

BOT_TOKEN = '7475649513:AAEsJXOJUXIO7kU5qebG9irpojqva7dwYlw'
ADMIN_ID = 352923545

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
router = Router()
# Регистрация обработчиков команд
    
register_handlers(router)
dp.include_router(router)

def isAdmin(id):
    if(ADMIN_ID == id):
        return True
    else:
        return False