#!/usr/bin/env python3
"""Async Comprehensions"""

async_generator = __import__('0-async_generator').async_generator
from typing import List, Generator


async def async_comprehension() -> List[Generator[float, None, None]]:
    """async_comprehension function"""
    data = [i async for i in async_generator()]

    return data
