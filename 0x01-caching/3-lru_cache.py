#!/usr/bin/env python3
"""" 3-lru_cache """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache
    """

    def __init__(self):
        """ Initialize
        """
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
            # Get the first key in the list
            firstKey = self.usedKeys.pop(0)
            # Delete the first key in the dictionary
            del self.cache_data[firstKey]
            print("DISCARD: {}".format(firstKey))

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            self.usedKeys.remove(key)
            self.usedKeys.append(key)
            return self.cache_data[key]
        return None
