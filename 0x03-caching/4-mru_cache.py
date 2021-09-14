#!/usr/bin/python3
""" MRU caching data
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU cache class"""

    def __init__(self):
        super().__init__()
        self.ordered_key = []

    def put(self, key, item):
        """Add a item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item

                else:
                    self.cache_data[key] = item
                    k = self.ordered_key[-1]
                    self.cache_data.pop(k)
                    self.ordered_key.append(key)
                    print(f"DISCARD: {k}")

            else:
                self.cache_data[key] = item

    def get(self, key):
        """get a item from the cache MRU algorithm"""
        if key is not None:
            get_key = self.cache_data.get(key, None)
            if get_key is not None:
                self.ordered_key.append(key)

            return get_key
