from functools import wraps
import logging
import time


def timeit(logger):
    def wrapper(fn):

        @wraps(fn)
        def inner_wrapper(*args, **kwargs):
            t0 = time.time()
            result = fn(*args, **kwargs)
            logger(f'{fn.__name__} took {time.time() - t0:.02f} seconds')
            return result
        return inner_wrapper
    return wrapper


@timeit(print)
def foo(n):
    time.sleep(n)
    return n


@timeit(logging.warning)
def bar(n):
    time.sleep(n)
    return n


def time_all(logger):
    def wrapper(cls):
        for name, obj in vars(cls).items():
            if not name.startswith('_') and callable(obj):
                setattr(cls, name, timeit(logger)(obj))
        return cls
    return wrapper


@time_all(print)
class Foo:
    def bar(self, n):
        time.sleep(n)
        return n

    def baz(self, n):
        m = n * 2
        time.sleep(m)
        return m
