from app.core.utils.base import time

# In memory cache implementation with TTL (default: 1 hr)
class Cache:

    def __init__(self):
        self._store = {}

    def set(
        self,
        key: str,
        value,
        ttl: int = 3600,
    ):

        self._store[key] = (
            value,
            time.time() + ttl,
        )

    def get(
        self,
        key: str,
    ):

        item = self._store.get(key)

        if item is None:
            return None

        value, expiry = item

        if time.time() > expiry:
            del self._store[key]
            return None

        return value