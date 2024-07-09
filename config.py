from DB.create import *
from DB.deleter import *
from DB.models import User
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

BOT_TOKEN = '7475649513:AAEsJXOJUXIO7kU5qebG9irpojqva7dwYlw'
ADMIN_ID = 352923545

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

def isAdmin(id):
    if(ADMIN_ID == id):
        return True
    else:
        return False