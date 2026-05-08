#!/usr/bin/env python3
"""Redis basic cache."""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class."""

    def __init__(self):
        """Initialize Redis client and flush the DB."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
