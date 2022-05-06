import json
import os
import aiohttp


async def get_available_bots():
    async with aiohttp.ClientSession() as session:
        async with session.post(os.environ['url_check_bots'],
                                data={'key': os.environ['adm_key']}) as response:
            response = json.loads(await response.text())
    if response['success']:
        bots = 'Вот список доступных ботов:\n'
        for i in response['bots']:
            bots += '`' + i + '`' + '\n'
        return {'Empty': False, 'bots': bots}
    else:
        return {'Empty': True}
