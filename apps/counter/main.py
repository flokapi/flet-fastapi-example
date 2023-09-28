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


@api.register
@app.get('/get-value')
async def get_value():
    return {'message': f'Counter value is currently {counter}'}


@api.register
@app.get('/set-value')
async def set_value(value: int):
    global counter
    counter = value
    return {'message': f'Updated counter value to {value}'}


async def main(page: ft.Page):
    await gui.init(page, api.get())

app.mount(f'/', flet_fastapi.app(main))
