import os
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=os.environ['token'])
dp = Dispatcher(bot, storage=storage)

ids = [
    int(os.environ['id_1']),
    int(os.environ['id_2']),
    int(os.environ['id_3']),
]
