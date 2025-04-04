from infrastucture import download_manifest

if __name__ == '__main__':
    manifest = download_manifest()
    print(manifest["Response"]['version'])

