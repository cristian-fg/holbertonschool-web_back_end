#!/usr/bin/env python3
"""Complex types (list of floats)"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum the list of floats

    Args:
    -> input_list list of floats

    returns
    -> the sum of the list
    """
    return sum(input_list)
