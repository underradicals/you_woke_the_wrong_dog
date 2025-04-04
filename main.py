from application import Manifest
from infrastucture import download_manifest

if __name__ == '__main__':
    manifest: Manifest = download_manifest()
    print(manifest['Response']['version'])