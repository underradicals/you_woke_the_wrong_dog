from typing import TypedDict
from typing_extensions import NotRequired


class FetchRequest(TypedDict):
  url: str
  from_cache: bool
  status: int
  content: str | bytes
  error: NotRequired[str]