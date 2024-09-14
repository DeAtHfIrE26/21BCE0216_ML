# cache.py
import redis

def get_redis_client():
    return redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def cache_set(key, value):
    redis_client = get_redis_client()
    redis_client.set(key, value)

def cache_get(key):
    redis_client = get_redis_client()
    return redis_client.get(key)
