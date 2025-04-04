from kernal.directories import ROOT
from .files import write_bytes, write_bytes_asjson
from .http import download_bytes
import orjson



def download_manifest(indent: bool=True):
  manifest_bytes = download_bytes('https://www.bungie.net/Platform/Destiny2/Manifest')
  bytes_array = [chunk for chunk in manifest_bytes]
  if indent:
    write_bytes_asjson(ROOT / 'manifest.json', bytes_array)
  else:
    write_bytes(ROOT / 'manifest.json', bytes_array)
  return orjson.loads(b''.join(bytes_array))