import os
import aiohttp
from aiogram.types import ReplyKeyboardRemove
from Commands import CheckForScreenshot


async def open_web(user_data, bot, message):
    if user_data["website"] == 'Садовник':
        async with aiohttp.ClientSession() as session:
            await session.post(os.environ['url_add_command'],
                               data={"bot_id": user_data['bot_id'],
                                     "key": os.environ['adm_key'],
                                     "command": user_data['command']})
            await session.post(os.environ['url_add_other_data'],
                               data={"bot_id": user_data['bot_id'],
                                     "key": os.environ['adm_key'],
                                     "website": os.environ['sadovnik']})

        await bot.send_message(message.from_user.id, "Команда на открытие сайта успешно отправлена!",
                               reply_markup=ReplyKeyboardRemove())

        await bot.send_message(message.from_user.id, "Ожидайте скриншота чтобы удостовериться в выполнении")

        await CheckForScreenshot.check_for_screenshot(user_data, bot, message)

    elif user_data["website"] == 'Завтра не наступит':
        async with aiohttp.ClientSession() as session:
            await session.post(os.environ['url_add_command'],
                               data={"bot_id": user_data['bot_id'],
                                     "key": os.environ['adm_key'],
                                     "command": user_data['command']})
            await session.post(os.environ['url_add_other_data'],
                               data={"bot_id": user_data['bot_id'],
                                     "key": os.environ['adm_key'],
                                     "website": os.environ['tommorow']})

        await bot.send_message(message.from_user.id, "Команда на открытие сайта успешно отправлена!",
                               reply_markup=ReplyKeyboardRemove())

        await bot.send_message(message.from_user.id, "Ожидайте скриншота чтобы удостовериться в выполнении")

        await CheckForScreenshot.check_for_screenshot(user_data, bot, message)

    else:
        async with aiohttp.ClientSession() as session:
            await session.post(os.environ['url_add_command'],
                               data={"bot_id": user_data['bot_id'],
                                     "key": os.environ['adm_key'],
                                     "command": user_data['command']})
            await session.post(os.environ['url_add_other_data'],
                               data={"bot_id": user_data['bot_id'],
                                     "key": os.environ['adm_key'],
                                     "website": user_data['website']})

        await bot.send_message(message.from_user.id, "Команда на открытие сайта успешно отправлена!",
                               reply_markup=ReplyKeyboardRemove())

        await bot.send_message(message.from_user.id, "Ожидайте скриншота чтобы удостовериться в выполнении")

        await CheckForScreenshot.check_for_screenshot(user_data, bot, message)
