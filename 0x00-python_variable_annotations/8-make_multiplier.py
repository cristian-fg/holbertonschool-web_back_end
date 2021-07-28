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
    def func(multiplier) -> float:
        """callable func

        Args:
        -> n number to mul

        return:
        -> the mul number
        """
        return multiplier * multiplier

    return func
