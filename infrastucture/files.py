from pathlib import Path
from typing import Iterator

import orjson


def write_bytes(filename: Path, iterator: Iterator[bytes] | list[bytes]):
  try:
    with open(filename, 'wb') as file:
      for chunk in iterator:
        file.write(chunk)
  except FileExistsError as e:
    print(e)
  except BlockingIOError as e:
    print(e)


def write_bytes_asjson(filename: Path, iterator: Iterator[bytes] | list[bytes]):
  try:
    bytes_string: bytes = bytes()
    with open(filename, 'wb') as file:
      for chunk in iterator:
        bytes_string += chunk
      file.write(orjson.dumps(orjson.loads(bytes_string), option=orjson.OPT_INDENT_2))
  except FileExistsError as e:
    print(e)
  except BlockingIOError as e:
    print(e)