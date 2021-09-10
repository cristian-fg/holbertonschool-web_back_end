#!/usr/bin/python3
""" LRU caching data
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class"""

    def __init__(self):
        super().__init__()
        self.ordered_key = []

    def put(self, key, item):
        """Add a item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    idx = self.ordered_key.index(key)
                    idx = self.ordered_key.pop(idx)
                    self.ordered_key.append(idx)
                else:
                    self.cache_data[key] = item
                    idx = self.ordered_key[0]
                    self.cache_data.pop(idx)

                    idx_value = self.ordered_key.index(idx)
                    self.ordered_key.pop(idx_value)
                    self.ordered_key.append(key)
                    print(f"DISCARD: {idx}")

            else:
                self.cache_data[key] = item
                self.ordered_key.append(key)

    def get(self, key):
        """get a item from the cache LRU algorithm"""
        if key is not None:
            get_key = self.cache_data.get(key, None)
            if get_key is not None:
                idx = self.ordered_key.index(key)
                idx = self.ordered_key.pop(idx)
                self.ordered_key.append(idx)

            return get_key
