import asyncio


from gui.counter import Counter



async def init(page, api):
    counter = Counter(api)
    await page.add_async(counter)
    await asyncio.create_task(counter.loop())
