#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random


async def async_generator():
    """generates a generator"""
    for i in range(10):
        await asyncio.sleep(1)
        n = random.uniform(0, 10)
        yield n
