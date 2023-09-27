import asyncio
import flet as ft


from gui.counter import Counter



async def idle(gui):
    while True:
        await gui.idle()
        await asyncio.sleep(5)


async def init(page, cfg, api):
    counter = Counter(cfg, api)
    await page.add_async(counter)
    await asyncio.create_task(idle(counter))
