import asyncio

async  def start_strongman(name, power):
    balls = [1, 2, 3, 4, 5]

    print(f'Силач {name} начал соревнования.')
    for i in balls:

        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')


async  def start_tournament():
    t1 = asyncio.create_task(start_strongman('Pypa', 2))
    t2 = asyncio.create_task(start_strongman('Lypa', 3))
    t3 = asyncio.create_task(start_strongman('Biba', 6))
    await t1
    await t2
    await t3


asyncio.run(start_tournament())


