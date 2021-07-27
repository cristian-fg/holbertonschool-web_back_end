#!/usr/bin/env python3
"""Complex types (list of floats)"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum the list of floats and ints

    Args:
    -> mxd_lst list of floats and ints

    returns
    -> the sum of the list
    """
    return sum(mxd_lst)
