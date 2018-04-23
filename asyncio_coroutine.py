import asyncio
import time

async def coroutine():
    print("in coroutine")
    time.sleep(5)

async def coroutine_ret():
    print("in coroutine")
    time.sleep(1)
    return 'result'

async def outer():
    print("in outer")
    print("waiting for result1")
    result1 = await phase1()
    print("waiting for result2")
    result2 = await phase2(result1)
    return result1, result2

async def phase1():
    print("in phase1")
    return 'result1'

async def phase2(arg):
    print("in phase2")
    return 'result2 derived from {}'.format(arg)

def basic():
    event_loop = asyncio.get_event_loop()
    try:
        print("starting coroutine")
        coro = coroutine()
        print("entering event loop")
        event_loop.run_until_complete(coro)
        #event_loop.call_later(5,coro)
    finally:
        print("closing event loop")
        event_loop.close()

def retval():
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(coroutine_ret())
        print("it returned: {!r}".format(return_value))
    finally:
        event_loop.close()

def chaining():
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        print('return value:{!r}'.format(return_value))
    finally:
        event_loop.close()

if __name__ == '__main__':
    #basic()
    #retval()
    chaining()

