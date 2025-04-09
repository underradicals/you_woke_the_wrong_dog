import asyncio
from enum import Enum
from typing import Any, Optional
import httpx
import redis.asyncio as redis

from kernal import Secrets
from .http_store import HttpStore

class StatusCodes:
    NOT_MODIFIES = 304
    OK = 200

# redis_client = redis.Redis(host="localhost", port=6379, db=0)
redis_client = HttpStore()

def deserialize_response(content: Optional[bytes]) -> None | str | bytes:
    """Deserialize content based on the type"""
    if content is None:
        return None
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError:
        return content 


def serialize_response(response: httpx.Response) -> bytes:
    """
        Serialize response based on content-type
        If the type cannot be determined just return content bytes
    """
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        return response.content
    elif "application/octet-stream" in content_type:
        return response.content
    else:
        # Fallback to bytes
        return response.content
    

async def fetch_cache_metadata(meta_key: str) -> dict[Any, Any] | Any:
    """Fetches metadata from store based on meta_key"""
    v: dict[Any, Any] | Any = await redis_client.hgetall(meta_key)
    return v

def check_for_last_modified(headers: dict, meta: dict):
    """Check for Last-Modified Header"""
    if b"Last-Modified" in meta:
        headers["If-Modified-Since"] = meta[b"Last-Modified"].decode()


def check_for_etag(headers: dict, meta: dict):
    """Check for ETag Header"""
    if b"ETag" in meta:
        headers["If-None-Match"] = meta[b"ETag"].decode()


async def store_meta_data(response: httpx.Response, meta_key: str):
    """Given a particula response and meta_key, store either Header Last-Modified or ETag"""
    new_meta = {}
    if "Last-Modified" in response.headers:
        new_meta["Last-Modified"] = response.headers["Last-Modified"]
    if "ETag" in response.headers:
        new_meta["ETag"] = response.headers["ETag"]

    if new_meta:
        await redis_client.hset(meta_key, new_meta)


async def get_cached_response(client: httpx.AsyncClient, url: str, cache_key: str, headers: dict):
    """
        If either If-Modified-Since or If-None-Match returns a 304 then return the cached data
    """
    cached_response = await redis_client.get(cache_key)
    return {
            "url": url,
            "name": 'world_content.zip' if url.endswith('content') else url.split("/")[-1].split("-")[0],
            "from_cache": True,
            "status": 304,
            "content": deserialize_response(cached_response),
            }
    



async def fetch_with_cache(
    urls: list[str],
    cache_prefix: str = "cache",
    timeout: float = 10.0,
    max_retries: int = 3,
    retry_delay: float = 1.0):
    async with httpx.AsyncClient(timeout=timeout, http2=True, base_url='https://www.bungie.net', follow_redirects=True) as client:
        tasks = [
            fetch(client, url, cache_prefix, max_retries, retry_delay)
            for url in urls
        ]
    return await asyncio.gather(*tasks)

    
async def fetch(client: httpx.AsyncClient,
                url: str,
                cache_prefix: str,
                max_retries: int,
                retry_delay: float):
    """Fetch resource at given url with built in retry and retry delay"""
    cache_key: str = f'{cache_prefix}:{url}'
    meta_key: str = f'{cache_key}:meta'
    
    meta: dict[Any, Any] | Any = await fetch_cache_metadata(meta_key)
    headers = {'x-api-key': Secrets.API_KEY }
    
    check_for_last_modified(headers, meta)
    check_for_etag(headers, meta)
    
    for attempt in range(1, max_retries + 1):
        try:
            response = await client.get(url, headers=headers)
            if response.status_code == StatusCodes.NOT_MODIFIES:
                return get_cached_response(client, url, cache_key, headers)
            
            content = serialize_response(response)
            await redis_client.set(cache_key, content)
            
            await store_meta_data(response, meta_key)
            
            return {
                "url": url,
                "name": 'world_content.zip' if url.endswith('content') else url.split("/")[-1].split("-")[0],
                "from_cache": False,
                "status": response.status_code,
                "content": deserialize_response(content),
            }
        except (httpx.RequestError, httpx.TimeoutException) as e:
            if attempt == max_retries:
                return {}
            await asyncio.sleep(retry_delay)
