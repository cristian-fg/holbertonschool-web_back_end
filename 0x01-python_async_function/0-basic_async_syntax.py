#!/usr/bin/env python3
"""The basics of async"""
import random


async def wait_random(max_delay: int = 10) -> float:
    return random.uniform(0, max_delay)
