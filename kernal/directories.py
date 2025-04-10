from pathlib import Path, PosixPath

class Directories:
    ROOT = Path().cwd()
    C_ROOT = PosixPath('/mnt/d/D2App/')
    DATA = C_ROOT / 'data'
    ASSETS = C_ROOT / 'assets'

if __name__ == '__main__':
    pass
