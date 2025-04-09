import asyncio
from orjson import loads

from application.FetchRequest import FetchRequest
from infrastructure import fetch_with_cache
from infrastructure import setup, write_archive, write_json_component_content_paths
from kernal import Directories

ENV = "Production"


def chunk_list(input_list, chunk_size):
    return [
        input_list[i : i + chunk_size] for i in range(0, len(input_list), chunk_size)
    ]


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


def get_manifest():
    if ENV == "Development":
        pass
    else:
        pass
        # get_manifest()


async def ingestion():
    setup()
    get_manifest()

    jwccp_values: list[str] = get_json_world_component_content_paths()

    results: list[FetchRequest] = await fetch_with_cache(jwccp_values)
    for result in results:
        content: str | bytes = result["content"]

        if result.get("error"):
            print(f"Error fetching {result['url']}: {result.get('error')}")

        if result["name"] == "world_content.zip":
            await write_json_component_content_paths(
                Directories.C_ROOT / f"{result['name']}", result, content
            )
            continue

        await write_json_component_content_paths(
            Directories.DATA / f"{result['name']}", result, content
        )

    write_archive()


async def main():
    await ingestion()


if __name__ == "__main__":
    asyncio.run(main())
