import os
import aiohttp
from aiogram.types import ReplyKeyboardRemove


async def close_current_window(user_data, bot, message):
    async with aiohttp.ClientSession() as session:
        await session.post(os.environ['url_add_command'],
                           data={"bot_id": user_data['bot_id'],
                                 "key": os.environ['adm_key'],
                                 "command": user_data['command']})

    await bot.send_message(message.from_user.id, "Команда на закрытие текущего открытого окна успешно отправлена!",
                           reply_markup=ReplyKeyboardRemove())
