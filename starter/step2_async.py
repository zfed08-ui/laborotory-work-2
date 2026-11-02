"""Шаг 2. Асинхронная программа: 10 задач выполняются конкурентно."""
import asyncio
from timer import print_time

async def work(n: int) -> None:
    print(f"start {n}")
    await asyncio.sleep(1)
    print(f"done {n}")

async def main() -> None:
    coroutines = [work(n) for n in range(1, 11)]
    await asyncio.gather(*coroutines)

if __name__ == "__main__":
    with print_time():
        asyncio.run(main())
