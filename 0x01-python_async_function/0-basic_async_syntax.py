#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """async random number"""
    number = random.uniform(0, max_delay)
    await asyncio.sleep(number)

    return number
