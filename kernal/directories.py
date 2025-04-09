from pathlib import Path, PosixPath

class Directories:
    ROOT = Path().cwd()
    C_ROOT = PosixPath('/mnt/d/D2App/')
    DATA = C_ROOT / 'data'

if __name__ == '__main__':
    pass
