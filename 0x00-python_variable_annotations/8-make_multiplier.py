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
        """callable func

        Args:
        -> n number to mul

        return:
        -> the mul number
        """
        return n * n

    return func
