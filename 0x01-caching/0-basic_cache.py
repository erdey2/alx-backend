#!/usr/bin/env python3
""" catching module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache extends BaseCaching """

    def put(self, key, item):
        """ add data to dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get data from a dictionary """
        return self.cache_data.get[key, None]
