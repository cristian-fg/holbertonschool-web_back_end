#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ multiple coroutines at the same time with async"""
    l = []

    for i in range(n):
        n_rand = await wait_random(max_delay)
        l.append(n_rand)

    return sorted(l)
