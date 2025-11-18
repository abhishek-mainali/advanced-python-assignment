import asyncio
async def count():
    print("counting started")
    await asyncio.sleep(1)
    print("counting finished")

    def on_complete():
        print("callback: counting is complete")

    async def main()
        await count()
        on_complete()

    asyncio.run(main())
