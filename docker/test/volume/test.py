#!/usr/bin/env python3

import pathlib

if __name__ == '__main__':
    path = '/root/kk/tmp.json'
    path = path.split("/")
    print(path)
    path = path[:len(path) - 1]
    path = '/'.join(path)
    print(path)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
