#!/usr/bin/env python3
"""type an iterable object"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length"""
    return [(i, len(i)) for i in lst]
