import os
import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?')

    return parser


def get_files(path):
    files_size_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = root + '\\' + file
            if files_size_dict.get((file, os.stat(filepath).st_size)):
                files_size_dict[(file, os.stat(filepath).st_size)].append(filepath)
            else:
                files_size_dict[(file, os.stat(filepath).st_size)] = [filepath]

    return files_size_dict


def get_duplicates_files(files):
    return [i for i in files.values() if len(i)>1]


if __name__ == '__main__':

    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.path:
        path = namespace.filepath
    else:
        path = input('Insert path:')

    files = get_files(path)

    duplicates_files = get_duplicates_files(files)

    if duplicates_files:
        print('Found:')
        print(duplicates_files)
    else:
        print('Not found.')