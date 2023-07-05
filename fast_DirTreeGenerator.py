import os
import sys

IGNORED_FOLDERS = ['.git', '.vscode', 'node_modules']


def create_folder_structure(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(os.path.basename(folder_path) + '\n')
        generate_structure(folder_path, f, '')


def generate_structure(folder_path, f, prefix):
    files = []
    dirs = []

    # Получаем список файлов и папок в данной директории
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            # Добавляем файлы в конец списка
            files.append(item)
        elif os.path.isdir(item_path):
            # Проверяем, игнорируемая ли это папка
            if item in IGNORED_FOLDERS:
                continue

            # Добавляем папки в конец списка
            dirs.append(item)

    # Выводим файлы в данной директории
    for i, file in enumerate(files):
        is_last_file = (i == len(files) - 1 and not dirs)
        file_prefix = '└──' if is_last_file else '├──'
        f.write(prefix + file_prefix + ' ' + file + '\n')

    # Рекурсивно обрабатываем папки
    for i, dir in enumerate(dirs):
        is_last_dir = (i == len(dirs) - 1)
        dir_prefix = '└──' if is_last_dir else '├──'
        f.write(prefix + dir_prefix + ' ' + dir + '\n')
        if is_last_dir:
            sub_prefix = prefix + '    '
        else:
            sub_prefix = prefix + '│   '

        generate_structure(os.path.join(folder_path, dir), f, sub_prefix)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python script.py <folder_path>')
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file = 'folder_structure.txt'

    create_folder_structure(folder_path, output_file)
