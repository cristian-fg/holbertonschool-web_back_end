#!/usr/bin/python3
""" Basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCahe"""

    def put(self, key, value):
        """Put a key/value pair into the cache."""
        if key is not None and value is not None:
            self.cache_data[key] = value

    def get(self, key):
        """get a key/value pair from the cache"""
        if key is not None:
            key_get = self.cache_data.get(key)
            return key_get
