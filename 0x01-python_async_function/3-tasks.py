#!/usr/bin/env python3
"""A function that creates a task for wait_random."""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a task that runs wait_random with the specified max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        asyncio.Task: The created asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))
