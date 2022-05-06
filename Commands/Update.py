import json
import os
import aiohttp


async def update(user_data, bot, message):
    async with aiohttp.ClientSession() as session:
        async with session.post(os.environ['url_update'],
                                data={'key': os.environ['adm_key'],
                                      'fname': user_data["fname"],
                                      'vcode': user_data["vcode"]}) as response:
            response = json.loads(await response.text())
    if response:
        await bot.send_message(message.from_user.id, 'Данные успешно отправлены')
    else:
        await bot.send_message(message.from_user.id, 'Данные не были отправлены')
