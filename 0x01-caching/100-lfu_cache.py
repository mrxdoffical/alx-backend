#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - inherits from BaseCaching
      - is a caching system using LFU algorithm with LRU as tiebreaker
    """
    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = defaultdict(int)
        self.freq_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def __update_freq(self, key):
        """Update the frequency of the key and adjust data structures
        """
        freq = self.keys_freq[key]
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.keys_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None

    def put(self, key, item):
        """ Add an item in the cache using LFU with LRU as tiebreaker
        Args:
            key: key to add
            item: value to add
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
                self.__update_freq(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Get the first key from the min frequency dict (LRU)
                    lfu_key = next(iter(self.freq_keys[self.min_freq]))
                    self.cache_data.pop(lfu_key)
                    del self.keys_freq[lfu_key]
                    del self.freq_keys[self.min_freq][lfu_key]
                    print("DISCARD: {}".format(lfu_key))
                self.min_freq = 0
                self.keys_freq[key] = 0
                self.freq_keys[0][key] = None
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key and update frequency
        Args:
            key: key to look for
        Returns:
            value associated with key if it exists, None otherwise
        """
        if key is not None and key in self.cache_data:
            self.__update_freq(key)
            return self.cache_data[key]
        return None
