import os
import aiohttp
from aiogram.types import ReplyKeyboardRemove
from Commands import CheckForScreenshot


async def open_notepad(user_data, bot, message):
    async with aiohttp.ClientSession() as session:
        await session.post(os.environ['url_add_command'],
                           data={"bot_id": user_data['bot_id'],
                                 "key": os.environ['adm_key'],
                                 "command": user_data['command']})
        await session.post(os.environ['url_add_other_data'],
                           data={"bot_id": user_data['bot_id'],
                                 "key": os.environ['adm_key'],
                                 "text": user_data["text"]})

    await bot.send_message(message.from_user.id, "Команда на открытие блокнота успешно отправлена!",
                           reply_markup=ReplyKeyboardRemove())

    await bot.send_message(message.from_user.id, "Ожидайте скриншота чтобы удостовериться в выполнении")

    await CheckForScreenshot.check_for_screenshot(user_data, bot, message)

