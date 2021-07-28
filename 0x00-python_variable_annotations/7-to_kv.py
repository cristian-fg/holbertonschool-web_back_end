#!/usr/bin/env python3
"""Complex types (string and int/float to tuple)"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """sum the list of floats and ints

    Args:
    -> k string
    -> v union of int and float

    returns
    -> tuple of str and square number
    """
    return (k, v**2)
