#!/usr/bin/env python3
"""Last-In First-Out Caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching Class which allows
    storing with a LIFO
    removal mechanism when the maximum item set is reached.
    """
    def __init__(self):
        """Initializes the Cache class Instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds to the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves from cache by key.
        """
        return self.cache_data.get(key, None)
