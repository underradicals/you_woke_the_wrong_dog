from typing import Any
import redis.asyncio as redis


class HttpStore:
  connection = redis.Redis(host="localhost", port=6379, db=0)
    
  async def set(self, cache_key: str, content: Any):
    await HttpStore.connection.set(cache_key, content)
    
  async def hgetall(self, meta_key: str):
    return await HttpStore.connection.hgetall(meta_key) # type: ignore
    
  async def hset(self, meta_key: str, new_data: dict):
    await HttpStore.connection.hset(meta_key, mapping=new_data) # type: ignore
    
  async def get(self, cache_key: str):
    return await HttpStore.connection.get(cache_key)