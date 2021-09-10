#!/usr/bin/python3
""" LIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache"""

    def __init__(self):
        super().__init__()
        self.last_key = []

    def put(self, key, item):
        """Add a item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.last_key.append(key)
                else:
                    self.cache_data.pop(self.last_key[-1])
                    print(f"DISCARD: {self.last_key[-1]}")
                    self.cache_data[key] = item
                    self.last_key.append(key)
            else:
                self.cache_data[key] = item
                self.last_key.append(key)

    def get(self, key):
        """get a item from the cache"""
        if key is not None:
            get_key = self.cache_data.get(key, None)
            return get_key
