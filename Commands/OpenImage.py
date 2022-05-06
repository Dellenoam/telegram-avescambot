import base64
import os
import aiohttp
from aiogram.types import ReplyKeyboardRemove
from Commands import CheckForScreenshot


async def open_image(user_data, bot, message):
    async with aiohttp.ClientSession() as session:
        await session.post(os.environ['url_add_command'],
                           data={'bot_id': user_data['bot_id'],
                                 'key': os.environ['adm_key'],
                                 'command': user_data["command"]})

    file_info = await bot.get_file(user_data['image'])
    downloaded_file = await bot.download_file(file_info.file_path)
    encoded_file = base64.b64encode(downloaded_file.getvalue())
    utf_decoded_file = encoded_file.decode("UTF-8")

    async with aiohttp.ClientSession() as session:
        await session.post(os.environ['url_add_other_data'],
                           data={'bot_id': user_data['bot_id'],
                                 'key': os.environ['adm_key'],
                                 'image': utf_decoded_file})

    await bot.send_message(message.from_user.id, "Команда на открытие изображения успешно отправлена!",
                           reply_markup=ReplyKeyboardRemove())

    await bot.send_message(message.from_user.id, "Ожидайте скриншота чтобы удостовериться в выполнении")

    await CheckForScreenshot.check_for_screenshot(user_data, bot, message)
