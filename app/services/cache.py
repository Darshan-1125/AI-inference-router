class SimpleCache:

    def __init__(self):
        self.cache = {}

    def get(self, query):
        return self.cache.get(query)

    def set(self, query, response):
        self.cache[query] = response

    def contains(self, query):
        return query in self.cache