#!/usr/bin/env python3
"""In this module we store information about how
many times we call a given URL"""


import requests
import redis
from typing import Callable
import functools


# Declare a redis handle
redis_h = redis.Redis()


def decorator(func: Callable) -> Callable:
    """Decorator function to wrap the actual function"""
    @functools.wraps(func)
    def wrapper(url):
        """Wrapper function that will wrap our
        callable func"""
        key = f"count:{url}"
        [
            redis_h.setex(key, 10, 1) if redis_h.get(key) is None
            else redis_h.set(key, int(redis_h.get(key)) + 1)
         ]
        return func(url)
    return wrapper


@decorator
def get_page(url: str) -> str:
    """Function to get the html of a page
    given the url"""
    response = requests.get(url)
    return response.text
