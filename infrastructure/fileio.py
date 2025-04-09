from pathlib import Path
from zipfile import ZipFile

import aiofiles
from application import FetchRequest
from kernal.directories import Directories
from kernal.strings import MagicStrings


def write_archive(dest: Path, source: Path):
    with open(dest, "wb") as db_file:
        with ZipFile(source, "r") as zip_file:
            for filename in zip_file.namelist():
                with zip_file.open(filename, "r") as archive:
                    db_file.write(archive.read())


async def write_json_component_content_paths(
    filepath: Path, result: FetchRequest, content: str | bytes
):
    async with aiofiles.open(filepath, "wb") as f:
        if isinstance(content, str):
            await f.write(content.encode("utf-8"))
        elif isinstance(content, bytes):
            await f.write(content)


def setup():
    if not Directories.DATA.exists():
        Directories.DATA.mkdir(exist_ok=True, parents=True)
