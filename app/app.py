import os

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiomysql.sa import create_engine

from db import DB_PASSWORD, DB_USER, DB_NAME
from .routes import setup_routes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


async def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))
    setup_routes(app)
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    app['db'] = await create_engine(
        host='127.0.0.1',
        port=3306,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        autocommit=True,
    )


async def on_shutdown(app):
    app['db'].close()
    await app['db'].wait_closed()
