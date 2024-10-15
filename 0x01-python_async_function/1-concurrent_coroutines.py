#!/usr/bin/env python3
"""an async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)."""
    delays = []

    results = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    for delay in results:
        insert_delay(delays, delay)

    return delays


# Helper function to insert delay in sorted order
def insert_delay(delays: List[float], delay: float) -> None:
    """ Insert delay in sorted order"""
    index = 0
    while index < len(delays) and delays[index] < delay:
        index += 1
    delays.insert(index, delay)
