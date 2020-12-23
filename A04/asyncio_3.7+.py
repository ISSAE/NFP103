import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main_seq():
    print(f"started at {time.strftime('%X')}")

    await say_after(2, 'hello')
    await say_after(3, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_seq())

async def main_para():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(3, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 3 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
   
asyncio.run(main_para())

async def main_para2():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(3, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 3 seconds.)
    done, pending = asyncio.wait(task1, task2, return_when=asyncio.ALL_COMPLETED)

    print(f"finished at {time.strftime('%X')}")
    print(done, pending)
   
asyncio.run(main_para2())
