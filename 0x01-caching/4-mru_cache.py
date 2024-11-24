#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache defines:
      - inherits from BaseCaching
      - is a caching system using MRU algorithm
    """
    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using MRU
        Args:
            key: key to add
            item: value to add
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(mru_key)
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key and update access order
        Args:
            key: key to look for
        Returns:
            value associated with key if it exists, None otherwise
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
