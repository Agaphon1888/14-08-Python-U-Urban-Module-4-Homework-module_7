# Домашнее задание по теме "Файлы в операционной системе".
# Задача - Освоить работу с файловой системой в Python, используя модуль os.

import os
import time

# Указываем директорию
directory = "."

# Обход каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        file_size = os.path.getsize(filepath)

        # Получаем родительскую директорию
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
