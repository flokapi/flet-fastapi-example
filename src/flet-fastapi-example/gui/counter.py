import flet as ft
import asyncio



class RequestCounter(ft.UserControl):
    def __init__(self, api):
        super().__init__()
        self.api = api

    async def update_count(self):
        count = await self.api['get_count']()
        self.text.value = f'Request Count: {count}'
        await self.update_async()

    async def idle(self):
        while True:
            await self.update_count()
            await asyncio.sleep(0.1)

    def build(self):
        self.text = ft.Text(style=ft.TextThemeStyle.HEADLINE_SMALL)

        return self.text