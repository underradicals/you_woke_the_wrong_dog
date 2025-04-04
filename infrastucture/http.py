from contextlib import contextmanager
from typing import Any, Generator
from requests import HTTPError, Session
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from requests.packages.urllib3.util.retry import Retry # type: ignore
from kernal import API_KEY

retries: Any = Retry(total=3, backoff_factor=0.1, status_forcelist=[500, 502, 503]) # type: ignore

session = Session()
session.mount(f"http://", HTTPAdapter(max_retries=retries)) # type: ignore

headers: dict[str, str] = {
    'x-api-key': API_KEY
}

@contextmanager
def request_executor(url: str) -> Generator[bytes, Any, Any]:
    try:
        with session.get(url, stream=True, allow_redirects=True, headers=headers) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                yield chunk
    except HTTPError as e:
        print(e)


def download_bytes(url: str) -> Generator[bytes, Any, Any]:
    try:
        with session.get(url, stream=True, allow_redirects=True, headers=headers) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                yield chunk
    except RequestException as e:
        print(e)


if __name__ == '__main__':
    pass
