#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - inherits from BaseCaching
      - is a caching system using FIFO algorithm
    """
    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using FIFO
        Args:
            key: key to add
            item: value to add
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))

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
