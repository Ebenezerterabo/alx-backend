#!/usr/bin/env python3
"""" 0-basic_cache """
# import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


# define BasicCache class
class BasicCache(BaseCaching):
    """ BasicCache defines:
        - constants of your caching system
        - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
