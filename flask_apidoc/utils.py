"""
Helpers.
"""

import functools


def cached(f):
    """
    Cache decorator for functions taking one or more arguments.
    :param f: The function to be cached.
    :return: The cached value.
    """

    cache = f.cache = {}

    @functools.wraps(f)
    def decorator(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]
    return decorator
