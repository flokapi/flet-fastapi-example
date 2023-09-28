from contextlib import asynccontextmanager
import flet as ft
import flet_fastapi
from fastapi import FastAPI

import gui
import api


@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()



app = FastAPI(lifespan=lifespan)

counter = 0


@app.get('/hello')
async def get_value():
    global counter
    counter += 1
    return {'message': 'Hi'}


@api.register
async def get_count():
    return counter


async def main(page: ft.Page):
    await gui.init(page, api.get())

app.mount(f'/', flet_fastapi.app(main))
