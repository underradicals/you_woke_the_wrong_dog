from typing import TypedDict
from typing_extensions import NotRequired


class FetchRequest(TypedDict):
  url: str
  name: str
  from_cache: bool
  status: int
  content: str | bytes
  error: NotRequired[str]