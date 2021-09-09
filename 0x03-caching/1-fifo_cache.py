#!/usr/bin/python3
""" FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put a key into the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys_sorted = sorted(self.cache_data.keys())
                self.cache_data.pop(keys_sorted[0])
                print(f"DISCARD: {keys_sorted[0]}")

    def get(self, key):
        """get a key from the cache"""
        if key is not None:
            get_key = self.cache_data.get(key, None)
            return get_key
