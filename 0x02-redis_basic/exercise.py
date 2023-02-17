#!/usr/bin/env python3
"""Redis basic"""
from functools import wraps
from readline import redisplay
from typing import Callable, Optional, Union
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """count function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call_history function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper method"""
        key_m = method.__qualname__
        inp_m = f'{key_m}:inputs'
        outp_m = f"{key_m}:outputs"
        data = str(args)
        self._redis.rpush(inp_m, data)
        fin = method(self, *args, **kwds)
        self._redis.rpush(outp_m, str(fin))
        return fin

    return wrapper


def replay(func: Callable):
    """replay function"""
    r = redis.Redis()
    key_m = func.__qualname__
    inp_m = r.lrange(f"{key_m}:inputs", 0, -1)
    outp_m = r.lrange(f"{key_m}:outputs", 0, -1)
    calls_number = len(inp_m)
    times_str = 'time' if calls_number == 1 else 'times'
    fin = f'{key_m} was called {calls_number} {times_str}:'
    print(fin)
    for k, v in zip(inp_m, outp_m):
        fin = f"{key_m}(*{k.decode('utf-8')}) -> {v.decode('utf-8')}"
        print(fin)


class Cache():
    """ class cache """
    def __init__(self):
        """init method """
        self._redis = redisplay.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Used to convert the data back to the desired format."""
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_int(self, key):
        return self.get(key, int)

    def get_str(self, key):
        value = self._redis.get(key)
        return value.decode("utf-8")
