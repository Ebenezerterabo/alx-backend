#!/usr/bin/env python3
""" 4-mru_cache """
from base_caching import BaseCaching


def MRUCache(BaseCaching):
    """ MRUCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        # Add or update item in the catch
        self.cache_data[key] = item
        # Update the used key list
        if key in self.usedKeys:
            self.usedKeys.remove(key)
        self.usedKeys.append(key)

        # Check if the cache is full
        if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
            # Get the last key in the list
            lastKey = self.usedKeys.pop()
            # Delete the last key in the dictionary
            del self.cache_data[lastKey]
            print("DISCARD: {}".format(lastKey))

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            self.usedKeys.remove(key)
            self.usedKeys.append(key)
            return self.cache_data[key]
        return None
