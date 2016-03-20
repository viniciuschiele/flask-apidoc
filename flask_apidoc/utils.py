"""
Helpers.
"""


def cached(f):
    """
    Cache decorator for functions taking one or more arguments.
    :param f: The function to be cached.
    :return: The cached value.
    """
    class CachedDict(dict):
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret

    return CachedDict(f)
