import asyncio


from gui.counter import RequestCounter



async def init(page, api):
    counter = RequestCounter(api)
    await page.add_async(counter)
    await asyncio.create_task(counter.idle())
