# import asyncio

# async def brew_chai():
#     print("Brwing chai...")
#     await asyncio.sleep(2)
#     print("Chai is ready")

# asyncio.run(brew_chai())


import asyncio


async def brew_chai():
    print("brewing Chai....")
    await asyncio.sleep(2)
    print("chai is ready")


asyncio.run(brew_chai())
