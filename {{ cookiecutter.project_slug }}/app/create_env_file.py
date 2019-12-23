import os
from pathlib import Path


def main():
    p = Path('.') / '.env'
    with open(p, 'w') as f:
        f.write(f'SECRET={os.urandom(64).hex()}')


if __name__ == '__main__':
    main()
