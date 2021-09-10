#!/usr/bin/python3
""" LRU caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU cache"""

    def __init__(self):
        super().__init__()
        self.ordered_dict = OrderedDict(self.cache_data)

    def put(self, key, item):
        """Add a item in the cache"""
        if key is not None and item is not None:
            self.ordered_dict[key] = item
            self.ordered_dict.move_to_end(key)

            if len(self.ordered_dict) > BaseCaching.MAX_ITEMS:
                k, _ = self.ordered_dict.popitem(last=False)
                print(f"DISCARD: {k}")
            self.cache_data = dict(self.ordered_dict)

    def get(self, key):
        """get a item from the cache LRU algorithm"""
        if key is not None:
            get_key = self.cache_data.get(key, None)
            if get_key is not None:
                self.ordered_dict.move_to_end(key)

            return get_key
