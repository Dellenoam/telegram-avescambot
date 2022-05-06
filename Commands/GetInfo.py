import os
import json
import aiohttp
from asyncio import sleep
from aiogram.types import ReplyKeyboardRemove


async def get_info(user_data, bot, message):
    async with aiohttp.ClientSession() as session:
        await session.post(os.environ['url_add_command'],
                           data={'bot_id': user_data['bot_id'],
                                 'key': os.environ['adm_key'],
                                 'command': user_data['command']})
    await bot.send_message(message.from_user.id, 'Команда на запрос данных о компьютере отправлена!',
                           reply_markup=ReplyKeyboardRemove())

    count = 0
    while count != 12:
        async with aiohttp.ClientSession() as session:
            async with session.post(os.environ['url_get_other_data'],
                                    data={'bot_id': user_data['bot_id'],
                                          'key': os.environ['adm_key'],
                                          'required': 'info'}) as response:
                response = json.loads(await response.text())

        if response["success"] and count <= 12:
            if user_data["bot_id"] == "ALL":
                await bot.send_message(message.from_user.id, "Вот информация со всех компьютеров")
                for item_info in response["info"]:
                    await bot.send_message(message.from_user.id, item_info)
                return
            else:
                await bot.send_message(message.from_user.id, "Вот информация о компьютере")
                return await bot.send_message(message.from_user.id, response['info'])
        elif count == 12:
            return await bot.send_message(
                message.from_user.id,
                "Невозможно получить скриншот. Не удалось получить получить дополнительные данные")
        else:
            count += 1
            await sleep(5)
