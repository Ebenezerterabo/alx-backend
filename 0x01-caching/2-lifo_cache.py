#!/usr/bin/env python3
""" 2-lifo_cache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the last key in the dictionary
                last_key = list(self.cache_data.keys())[-1]
                # Remove the last key in the dictionary
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
