#!/usr/bin/env python3
"""Basic caching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Simple Caching Class with basic
    storing and retrieving
    """

    def put(self, key, item):
        """Adds to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves from cache by key.
        """
        return self.cache_data.get(key, None)
