"""Дополнительный шаг: что будет, если одна задача надолго займёт event loop."""
import asyncio
from concurrent.futures import ProcessPoolExecutor
from timer import log, print_time

CLIENTS = [
    ("alice", 0.5),
    ("bob", 5.0),
    ("carol", 0.5),
    ("dave", 0.5),
    ("eve", 0.5),
]

# Для задания 4в можно добавить сюда "dave" и "eve".
HEAVY_CLIENTS = {"bob"}

# True — использовать отдельный процесс, False — отдельный поток.
USE_PROCESS = True


def heavy_compute() -> int:
    h = 0
    for i in range(30_000_000):
        h = (h * 31 + i) & 0xFFFFFFFF
    return h


async def handle_request(client, duration, pool):
    log(f"{client}: запрос принят")

    if client in HEAVY_CLIENTS:
        if USE_PROCESS:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(pool, heavy_compute)
        else:
            await asyncio.to_thread(heavy_compute)
    else:
        await asyncio.sleep(duration)

    log(f"{client}: ответ отправлен")


async def main():
    with ProcessPoolExecutor() as pool:
        tasks = [
            handle_request(client, duration, pool)
            for client, duration in CLIENTS
        ]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    with print_time():
        asyncio.run(main())
