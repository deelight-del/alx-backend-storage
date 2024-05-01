#!/usr/bin/env python3
"""In this module, we create a Cache class that
implements the redis-py package, imported as redis"""


import redis
import uuid
from typing import Union


class Cache:
    """A Cache class expected to work as a caching system"""
    def __init__(self):
        """The initialization method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        """store method that takes a data
        argument and returns a string"""
        random_string = uuid.uuid4()
        self._redis.set(random_string, data)
        self._redis.bgsave()
        return random_string
