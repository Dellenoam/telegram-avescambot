from aiogram import types
from aiogram.utils import executor
from create_bot import bot, dp, ids
from Handler import start_handler, commands_handler


# Сообщение о запуске
async def on_startup(_):
    for i in ids:
        await bot.send_message(i, 'Бот запущен!')


# Стартовая часть (список команд, получение информации о том как работать и т.д)
start_handler.register_start_handler(dp)

# Основная часть
commands_handler.register_commands_handler(dp)


# Ответ по умолчанию на неизвестные команды
@dp.message_handler()
async def default(message: types.Message):
    if message.from_user.id in ids:
        await bot.send_message(message.from_user.id,
                               'Используйте /start или /help, чтобы узнать как пользоваться ботом')


# Запуск бота
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
