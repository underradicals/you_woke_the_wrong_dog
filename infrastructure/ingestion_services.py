import asyncio
from pathlib import PosixPath
import sqlite3
from typing import Any
from orjson import loads

from application import FetchRequest
from infrastructure import fetch_with_cache, get_manifest
from infrastructure import setup, write_archive, write_json_component_content_paths
from kernal import Directories, MagicStrings, chunk_list
from .image_ingestion_repository import iter_gen, fetch_all_damage_types, fetch_all_icons, fetch_all_screenshots, fetch_all_watermarks, fetch_images


ENV = "Development"
resource_list = []

def dict_factory(cursor: sqlite3.Cursor, row: list[Any]) -> dict[str | Any, Any]:
    fields = [x[0] for x in cursor.description]
    return dict(zip(fields, row))

d2_connection = sqlite3.connect("/mnt/d/D2App/d2.db")
d2_connection.execute("pragma journal_mode=Wal")
d2_connection.row_factory = dict_factory


def get_json_world_component_content_paths() -> list[str]:
    with open("manifest.json", "rb") as manifest_string:
        manifest_json = loads(manifest_string.read())
        manifest_response = manifest_json["Response"]

        jwccp_values = [
            x
            for x in {
                x: y
                for x, y in manifest_response["jsonWorldComponentContentPaths"][
                    "en"
                ].items()
            }.values()
        ]
        jwccp_values.append(manifest_response["mobileWorldContentPaths"]["en"])
        return jwccp_values


def manifest():
    if ENV == "Development":
        pass
    else:
        pass
        get_manifest()


async def ingestion():
    setup()
    manifest()

    jwccp_values: list[str] = get_json_world_component_content_paths()

    results: list[FetchRequest] = await fetch_with_cache(jwccp_values)
    for result in results:
        content: str | bytes = result["content"]

        if result.get("error"):
            print(f"Error fetching {result['url']}: {result.get('error')}")
        
        if result["url"].endswith('content'):
            await write_json_component_content_paths(
                Directories.C_ROOT / "world_content.zip", result, content
            )
            continue

        await write_json_component_content_paths(
            Directories.DATA / f"{result["url"].split("/")[-1]}", result, content
        )

    write_archive(MagicStrings.WORLD_CONENT_DB, MagicStrings.WORLD_CONTENT_ZIP)


async def image_ingestion():
    iter_gen(fetch_all_icons(d2_connection), "icon_url", resource_list)
    iter_gen(fetch_all_watermarks(d2_connection), "watermark_url", resource_list)
    iter_gen(fetch_all_screenshots(d2_connection), "screenshot_url", resource_list)
    iter_gen(fetch_all_damage_types(d2_connection), "damage_type_url", resource_list)

    for chunk in fetch_images(chunk_list(resource_list, 100)):
        for item in chunk:
            url_parts = item.split("/")
            name = url_parts.pop()
            stem = '/'.join(url_parts)
            directory = f'{Directories.ASSETS}{stem}'
            print(f'{name} -- {stem} -- {directory}')
        results = await fetch_with_cache(chunk)
        for result in results:
            content: str | bytes = result["content"]

            if result.get("error"):
                print(f"Error fetching {result['url']}: {result.get('error')}")

            url_parts = result["url"].split("/")
            name = url_parts.pop()
            stem = '/'.join(url_parts)
            directory = PosixPath(f'{Directories.ASSETS}{stem}')
            
            if not directory.exists():
                directory.mkdir(exist_ok=True, parents=True)
            
            await write_json_component_content_paths(
                directory / f"{name}", result, content
            )
        await asyncio.sleep(1)



if __name__ == "__main__":
    pass
