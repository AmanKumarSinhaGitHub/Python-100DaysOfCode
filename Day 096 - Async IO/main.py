import asyncio

async def my_async_function1():
    print("Start function 1")
    await asyncio.sleep(2)
    print("End function 1")
    return "Result from function 1"

async def my_async_function2():
    print("Start function 2")
    await asyncio.sleep(1)
    print("End function 2")
    return "Result from function 2"

async def main():
    results = await asyncio.gather(
        my_async_function1(),
        my_async_function2()
    )
    print("All functions are done.")
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
