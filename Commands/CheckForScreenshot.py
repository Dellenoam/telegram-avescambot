import json
import os
import aiohttp
from asyncio import sleep


async def check_for_screenshot(user_data, bot, message):
    count = 0
    while count <= 12:
        async with aiohttp.ClientSession() as session:
            async with session.post(os.environ['url_get_other_data'],
                                    data={'bot_id': user_data['bot_id'],
                                          'key': os.environ['adm_key'],
                                          'required': 'screenshot'}) as response:
                response = json.loads(await response.text())

        if response['success'] and count != 12:
            url = 'https://api.imgbb.com/1/upload'
            if user_data["bot_id"] == "ALL":
                for item_screenshot in response["screenshot"]:
                    payload = {
                        'key': os.environ['api_key'],
                        'image': item_screenshot,
                        'expiration': 120
                    }

                    async with aiohttp.ClientSession() as session:
                        async with session.post(url, data=payload) as response:
                            response = json.loads(await response.text())

                    if response["success"]:
                        await bot.send_photo(message.from_user.id, response["data"]["url"])
                    else:
                        await bot.send_message(message.from_user.id,
                                               "Невозможно получить скриншот. Ошибка при загрузке на imgbb")
                return
            else:
                payload = {
                    'key': os.environ['api_key'],
                    'image': response["screenshot"],
                    'expiration': 120
                }

                async with aiohttp.ClientSession() as session:
                    async with session.post(url, data=payload) as response:
                        response = json.loads(await response.text())
                if response["success"]:
                    return await bot.send_photo(message.from_user.id, response["data"]["url"])
                else:
                    return await bot.send_message(message.from_user.id,
                                                  "Невозможно получить скриншот. Ошибка при загрузке на imgbb")
        elif count == 12:
            return await bot.send_message(
                message.from_user.id,
                "Невозможно получить скриншот. Не удалось получить получить дополнительные данные")
        else:
            count += 1
            await sleep(5)
