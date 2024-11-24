#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - inherits from BaseCaching
      - is a caching system using LIFO algorithm
    """
    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache using LIFO
        Args:
            key: key to add
            item: value to add
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data):
                if self.last_key is not None:
                    self.cache_data.pop(self.last_key)
                    print("DISCARD: {}".format(self.last_key))
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key
        Args:
            key: key to look for
        Returns:
            value associated with key if it exists, None otherwise
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
