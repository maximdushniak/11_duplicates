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
        for particular_file in files:
            filepath = root + '\\' + particular_file
            if files_size_dict.get((particular_file, os.stat(filepath).st_size)):
                files_size_dict[(particular_file, os.stat(filepath).st_size)].append(filepath)
            else:
                files_size_dict[(particular_file, os.stat(filepath).st_size)] = [filepath]

    return files_size_dict


if __name__ == '__main__':

    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.path:
        path = namespace.filepath
    else:
        path = input('Введите путь к папке:')

    files = get_files(path)

    duplicates_files = list(filter(lambda x: len(files[x]) > 1, files))

    if duplicates_files:
        print('Найдено {} дубль(ей):'.format(len(duplicates_files)))
        for duplicate in duplicates_files:
            print(duplicate[0], "({} byte)".format(duplicate[1]), files[duplicate])
    else:
        print('Дупликаты файлов не найдены.')
