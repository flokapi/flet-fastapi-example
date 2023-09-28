import flet as ft
import asyncio



class Counter(ft.UserControl):
    def __init__(self, api):
        super().__init__()
        self.api = api

    async def minus(self):
        self.txt_number.value = str(int(self.txt_number.value) - 1)
        await self.update_async()

    async def plus(self):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        await self.update_async()

    async def publish(self):
        await self.api['set_value'](int(self.txt_number.value))

    async def idle(self):
        while True:
            await self.plus()
            await asyncio.sleep(5)

    def build(self):
        async def minus_click(e):
            await self.minus()

        async def plus_click(e):
            await self.plus()

        async def publish_click(e):
            await self.publish()

        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
        
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                        self.txt_number,
                        ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton('Publish', on_click=publish_click)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        )