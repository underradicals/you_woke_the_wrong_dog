from typing import Any
from redis import Redis
from infrastructure import ArgumentEmptyException
from kernal import MagicStrings, Secrets
from requests import HTTPError, get, Session, head
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

session = Session()
retries = Retry(
    total=5,
    backoff_factor=0.1,
    raise_on_redirect=False,
    backoff_jitter=2,
    status_forcelist=[500, 501, 503, 504],
)
session.mount("https://", adapter=HTTPAdapter(max_retries=retries))
redis_connection = Redis(host="localhost", port=6379, decode_responses=True)
request_headers = {
    'x-api-key': Secrets.API_KEY,
}

def get_last_modified(cache_key: str) -> str | None:
    v = redis_connection.get(f"{cache_key}.last-modified")
    if v is None:
        return None
    return str(v)

def set_if_modified_since(url: str):
    with head(f'{MagicStrings.BASE_ADDRESS}{url}', allow_redirects=True) as head_response:
            request_headers.update({
                'If-Modified-Since': head_response.headers['Last-Modified']
            })
            

def set_last_modified(cache_key: str, headers: dict[str, Any]):
    redis_connection.set(f'{cache_key}.last-modified', headers['Last-Modified'])


def request(url: str, cache_key: str):
    with get(f'{MagicStrings.BASE_ADDRESS}{url}', allow_redirects=True, headers=request_headers) as response:
        response.raise_for_status()
        if response.status_code == 304:
            return
        set_last_modified(cache_key, dict(response.headers))
        return response.content


def download(url: str, cache_key: str):
    """
    Description:
        To download a resource, or not when the resource has not changed --
        To make a robust method for handling frequent requests to the D2 servers we must address several pain points when dealing with
        stale data and data that changes often.
    Parameters:
        url (str): -- The url to the resource we are downloading
        cache_key (str): -- The leading identifier for the keys submitted to the Store particular to `this` request e.g. `(url)`.
    Returns: 
        bytes
    Raises:
        ArgumentEmptyException: Signature cannot be empty or None
    """
    
    try:
        if url == "" or cache_key == "":
            raise ArgumentEmptyException("Signature cannot be empty or None")
        
        # Check Store for Last-Modified Header
        last_modified = get_last_modified(cache_key=cache_key)
        
        if last_modified is None:
            # Make the request and record last-modified: Nothing exist in the store
            return request(url, cache_key)

        set_if_modified_since(url)
        return request(url, cache_key)

    except ArgumentEmptyException as e:
        print(e)
    except HTTPError as e:
        print(e)


if __name__ == "__main__":
    download('/common/destiny2_content/json/en/DestinyDamageTypeDefinition-c7d255e4-54c1-4a34-b87e-f64c2ba9f977.json', "damage_type_def")
