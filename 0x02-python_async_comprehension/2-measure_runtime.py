#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure time"""
    s = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(3)))
    elapsed = time.time() - s

    return elapsed
