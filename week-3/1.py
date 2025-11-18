import asyncio
import time

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

async def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(letter)
        await asyncio.sleep(1.5)

async def main():
    start = time.time()

    await asyncio.gather(
        print_numbers(),
        print_letters()
    )

    end = time.time()
    print("Total time:", end - start)

asyncio.run(main())