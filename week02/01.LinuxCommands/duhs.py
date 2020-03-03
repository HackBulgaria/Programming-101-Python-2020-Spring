import os
import sys

DIR_INIT_SIZE = 2 * 4096


def get_file_disk_usage(filepath):
    blocks_used = (os.stat(filepath).st_size // 4096) + 1
    return blocks_used * 4  # KB


def get_files_size(path):
    if os.path.isfile(path):
        return get_file_disk_usage(path)

    total = 0

    if os.path.isdir(path):
        for inner in os.scandir(path):
            if inner.is_file():
                total += os.stat(inner).st_size
            if inner.is_dir():
                total += get_files_size(inner)

    return total


def get_dirs_size(path):
    counter = 0
    if os.path.isdir(path):
        counter = sum([1 for _ in os.walk(path)])

    return counter * DIR_INIT_SIZE


def duhs(path):
    dirs_size = get_dirs_size(path)
    files_size = get_files_size(path)

    return dirs_size + files_size


def main():
    size = duhs(sys.argv[1])
    print(f'{size // 1024}K')

    return size


if __name__ == '__main__':
    main()
