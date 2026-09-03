import redis


class RedisCache:

    def __init__(self):
        self.client = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )

    def _normalize_key(self, query):
        return query.strip().lower().rstrip("?!.,")

    def get(self, query):
        key = self._normalize_key(query)
        return self.client.get(key)

    def set(self, query, response):
        key = self._normalize_key(query)
        self.client.set(key, response)

    def contains(self, query):
        key = self._normalize_key(query)
        return self.client.exists(key) > 0