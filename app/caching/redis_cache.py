import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def cache_set(key: str, value: str):
    r.set(key, value)

def cache_get(key: str):
    return r.get(key)
