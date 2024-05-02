#!/usr/bin/env python3
"""In this module, we create a Cache class that
implements the redis-py package, imported as redis"""


import redis
import uuid
from typing import Union, Callable, Any, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """A decorator function that counts number of times
    that a method has been called"""

    # Functool wraps method to preserve ppties of wrapped function
    @functools.wraps(method)
    # Wrapper Function to increase number of times func is called
    def wrapper_count_calls(self, *args, **kwargs):
        """Inner wrapper function to modify the methods of Cache"""
        # args[0] should be ``self``
        # We then use self to access redis and increase the __qualname__
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper_count_calls


class Cache:
    """A Cache class expected to work as a caching system"""
    def __init__(self):
        """The initialization method"""
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data
        argument and returns a string"""
        random_string = str(uuid.uuid4())
        self._redis.set(random_string, data)
        return random_string

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Optional[Any]:
        """Defining the get method."""
        if self._redis.get(key) is not None:
            return (
                self._redis.get(key)
                if fn is None
                else fn(self._redis.get(key))
            )
        return None

    def get_str(self, key: str):
        """Use Cache.get to convert to str"""
        self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str):
        """Use Cache.get to convert to int"""
        self.get(key, int)
