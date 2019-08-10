import json
from asyncio import sleep

import aiohttp
import aiohttp_jinja2

import db


@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    pass


async def websocket_user_data_handler(request):
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                data = json.loads(msg.data)
                async with request.app['db'].acquire() as connection:
                    await connection.execute(
                        db.users.insert().values(
                            name=data['name'],
                            age=int(data['age']),
                            city=data['city']
                        )
                    )
                await sleep(10)
                await ws.send_str('Your data success saved')
    return ws
