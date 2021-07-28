#!/usr/bin/env python3
"""Complex types (functions)"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier float number

    Args:
    -> multiplier a float

    returns
    -> a function callable
    """
    def func(n: float) -> float:
        return n * n

    return func
