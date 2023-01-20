
import asyncio

async def main():
    parallel_task = asyncio.create_task(parallel_fun2())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await asyncio.sleep(1)
    print("C")
    await asyncio.sleep(1)
    print("D")
    await asyncio.sleep(1)
    print("E")


async def parallel_fun2():
    print("AA")
    await asyncio.sleep(1)
    print("BB")
    await asyncio.sleep(1)
    print("CC")
    await asyncio.sleep(1)
    print("DD")
    await asyncio.sleep(1)
    print("EE")

    return 10

asyncio.run(main())