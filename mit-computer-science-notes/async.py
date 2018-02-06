import asyncio


async def hello():
    print('hello world')
    r = await asyncio.sleep(1)
    print('hello again')


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
