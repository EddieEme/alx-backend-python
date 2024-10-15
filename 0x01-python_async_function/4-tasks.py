#!/usr/bin/env python3
"""A function that spawns multiple tasks using task_wait_random."""

import asyncio
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n tasks that run wait_random using task_wait_random.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays (float values) from the tasks.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
