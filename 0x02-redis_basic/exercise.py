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

    key = method.__qualname__
    # Functool wraps method to preserve ppties of wrapped function

    # Wrapper Function to increase number of times func is called
    @functools.wraps(method)
    def wrapper_count_calls(self, *args, **kwargs):
        """Inner wrapper function to modify the methods of Cache"""
        # args[0] should be ``self``
        # We then use self to access redis and increase the __qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_count_calls


def call_history(method: Callable) -> Callable:
    """Decorator to store the input and output
    history of the calls into a redis list"""
    # Create the namespaces for input and output key.
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    # Preserve method meta properties.
    @functools.wraps(method)
    def wrapper_call_history(self, *args, **kwargs):
        """Wrapper function to manipulate the method"""
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper_call_history


def replay(method: Callable):
    """Function that takes a callable and replays
    the behaviour of the callable"""
    redis_h = redis.Redis(host='localhost', port=6379)
    qualname = method.__qualname__
    call_count = redis_h.get(qualname)
    print(f"{qualname} was called {call_count.decode('utf-8')} times:")
    for inputs, outputs in zip(
        redis_h.lrange(f"{qualname}:inputs", 0, -1),
        redis_h.lrange(f"{qualname}:outputs", 0, -1)
    ):
        print(
            """{}(*{}) -> {}""".format(
                qualname,
                inputs.decode('utf-8'),
                outputs.decode('utf-8')
            )
        )


class Cache:
    """A Cache class expected to work as a caching system"""
    def __init__(self):
        """The initialization method"""
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    @call_history
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
