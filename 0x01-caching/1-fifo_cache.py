#!/usr/bin/env python3
""" 1-fifo_cache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ delete the first item in the cache (FIFO algorithm)
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the first key in the dictionary
                first_key = list(self.cache_data.keys())[0]
                # Remove the first key in the dictionary
                del self.cache_data[first_key]
                # Print the discarded key
                print("DISCARD: {}".format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
