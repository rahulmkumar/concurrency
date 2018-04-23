import asyncio

def mark_done(future, result):
    print('setting future result to {}'.format(result))
    future.set_result(result)

event_loop = asyncio.get_event_loop()

try:
    all_done = asyncio.Future()

    print('scheduling mark done')
    event_loop.call_soon(mark_done, all_done, 'the result')

    print('entering event loop')

    result = event_loop.run_until_complete(all_done)
    print('returned result:{}'.format(result))
finally:
    print('closing event loop')
    event_loop.close()

print('future result: {}'.format(all_done.result()))
