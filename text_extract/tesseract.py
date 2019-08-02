import asyncio


async def count():
    print("One")
    print('a')
    print("Two")


async def main():
    await asyncio.wait([count(), count(), count()])
    return 1


loop = asyncio.get_event_loop()
a = loop.run_until_complete(main())
print(a)