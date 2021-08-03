#!/usr/bin/env python3
"""The basics of async"""
import random


async def fun_rand(delay):
    return random.uniform(0, delay)


async def wait_random(max_delay: int = 10) -> float:
    """async random number"""
    return await fun_rand(max_delay)
