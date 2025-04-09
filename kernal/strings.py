from pathlib import Path, PosixPath, WindowsPath


class MagicStrings:
    BASE_ADDRESS = "https://www.bungie.net"
    MANIFEST_URL_PATH = f"{BASE_ADDRESS}/Platform/Destiny2/Manifest"
    ROOT = Path().cwd()
    MANIFEST_PATH = PosixPath('/mnt/d/D2App/manifest.json')
    WORLD_CONTENT_ZIP = PosixPath('/mnt/d/D2App/world_content.zip')
    WORLD_CONENT_DB = PosixPath('/mnt/d/D2App/world_content.db')


if __name__ == "__main__":
    pass
