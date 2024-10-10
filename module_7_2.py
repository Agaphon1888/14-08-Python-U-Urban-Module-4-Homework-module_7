# Домашнее задание по теме "Позиционирование в файле".
# Задача "Записать и запомнить".

def custom_write(file_name, strings):
    # Создаем пустой словарь для хранения позиций строк.
    strings_positions = {}

    # Открываем файл в режиме записи с кодировкой utf-8.
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):       # про enumerate - это с "хабра" взято:
                                                                # https://habr.com/ru/companies/ruvds/articles/485648/
            # Получаем текущую позицию в байтах перед записью.
            byte_position = file.tell()
            # Записываем строку в файл, добавляя переход на новую строку.
            file.write(string + '\n')
            # Сохраняем позицию и строку в словаре.
            strings_positions[(index, byte_position)] = string

    return strings_positions


# Пример использования функции.
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)