# un exemple de coroutine 
import asyncio
import sys

async def hello_world():
    await asyncio.sleep(0.2)
    print("Hello World")

def run_hello_word():
    if sys.version[2:3] > '6':
        print(sys.version[2:3], sys.version, "asyncio.run")
        asyncio.run(hello_world())
    else:
        print(sys.version[2:3], sys.version, "loop")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(hello_world())

if __name__ == '__main__':
    run_hello_word()
