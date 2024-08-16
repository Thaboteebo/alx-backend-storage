#!/usr/bin/env python3
"""

"""

import redis
import uuid
from typing import Union, Optional, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs): #soucer skip: avoid-builtin-shadow
       """
       """
       key = method.__qualname__
       self._redis.incr(key)
       
       return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    """
    call_history function
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs): #soucery skip: avoid-builtin-shadow
        """
        wrapper function
        """
        base_key = method.__qualname__
        inputs_key = f"{base_key}:inputs"
        outputs_key = f"{base_key}:outputs"

        input_data = str (args)
        self._redis.rpush(inputs_key, input_data)

        output = method(self, *args, **kwargs)

        output_data = str(output)
        self._redis.rpush(outputs_key, output_data)

        return output

    return wrapper

class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """
        """
        self._redis = redis.Redis(host=host, port=port, db=db)
        self._redis.flushdb()


    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """

        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        """
        data = self._redis.get(key)

        if data is None:
            return data

        if fn:
            callable_fn = fn(data)
            return callable_fn
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        """
        value = self._redis.get(key, fn=lambda d: d.decode("utf-8"))
        return value

    def get_int(self, key: str) -> int:
        """
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            return None

        return value
