"""Шаг 1. Синхронная программа."""
import time
from timer import print_time

def work(n: int) -> None:
    print(f"start {n}")
    time.sleep(1)
    print(f"done {n}")

def main() -> None:
    for n in range(1, 11):
        work(n)

if __name__ == "__main__":
    with print_time():
        main()
