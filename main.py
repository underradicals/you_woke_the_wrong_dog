from zipfile import ZipFile
import httpx
import asyncio
import redis.asyncio as redis
from typing import Optional, TypedDict
from orjson import loads, dumps
import aiofiles

from infrastructure import fetch_with_cache
from kernal import Directories
from kernal import MagicStrings

ENV = 'Production'

class GlobalState(TypedDict):
    world_content_url: str
    json_world_component_content_paths: dict
    

global_state = {
    'world_content_url': '',
    'json_world_component_content_paths': dict()
}

def chunk_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

async def ingestion():
    if not Directories.DATA.exists():
        Directories.DATA.mkdir(exist_ok=True, parents=True)
    if ENV == 'Development':
        pass
    else:
        pass
        # get_manifest()
    max_workers = 5
    with open("manifest.json", "rb") as manifest_string:
        manifest_json = loads(manifest_string.read())
        manifest_response = manifest_json['Response']
        
        global_state['world_content_url'] = f'{MagicStrings.BASE_ADDRESS}{manifest_response['mobileWorldContentPaths']['en']}'
        global_state['json_world_component_content_paths'] = {x: y for x, y in manifest_response['jsonWorldComponentContentPaths']['en'].items()}
        
        jwccp_keys = [Directories.DATA / f'{x}.json' for x in global_state['json_world_component_content_paths'].keys()]
        jwccp_keys.append(Directories.C_ROOT / 'world_content.zip')
        
        jwccp_values = [x for x in global_state['json_world_component_content_paths'].values()]
        jwccp_values.append(global_state['world_content_url'])


    results = await fetch_with_cache(jwccp_values)
    for result in results:
        content = result["content"] # type: ignore
        if result.get('error'):
            print(f"Error fetching {result['url']}: {result['error']}") # type: ignore
        if result['name'] == 'world_content.zip': # type: ignore
            async with aiofiles.open(Directories.C_ROOT / f'{result['name']}', "wb") as f: # type: ignore
                if isinstance(content, str):
                    await f.write(content.encode("utf-8"))
                elif isinstance(content, bytes):
                    await f.write(content)
        else:    
            async with aiofiles.open(Directories.DATA / f'{result['name']}', "wb") as f: # type: ignore
                if isinstance(content, str):
                    await f.write(content.encode("utf-8"))
                elif isinstance(content, bytes):
                    await f.write(content)
        print(f"Downloaded File: {result['name']} -> {result['status']}") # type: ignore
    
    with open(MagicStrings.WORLD_CONENT_DB, 'wb') as db_file:
        with ZipFile(MagicStrings.WORLD_CONTENT_ZIP, 'r') as zip_file:
            filename = zip_file.namelist()[0]
            with zip_file.open(filename, 'r') as archive:
                db_file.write(archive.read())


if __name__ == "__main__":
    asyncio.run(ingestion())