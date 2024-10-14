# Домашнее задание по теме "Оператор "with".
# Задача "Найдёт везде".

class WordsFinder:
    trans_table = str.maketrans('.!,:;=?', '       ')  # таблица преобразования для str.translate

    def __init__(self, *file_names: str):
        self.file_names = file_names
        self.all_words = self.get_all_words()  # Сохранение всех слов сразу

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                    content = content.lower() \
                        .replace(' - ', ' ') \
                        .translate(self.trans_table)
                    content = ' '.join(content.split())
                    all_words[file_name] = content.split()
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []  # Добавить пустой список на случай отсутствия файла
        return all_words

    def find(self, search_word: str):
        search_word = search_word.lower()
        found_words = {}
        for file_name, words in self.all_words.items():
            if search_word in words:
                found_words[file_name] = words.index(search_word) + 1  # позиция начинается с 1
        return found_words

    def count(self, search_word: str):
        search_word = search_word.lower()
        word_number = {file_name: words.count(search_word) for file_name, words in self.all_words.items()}
        return word_number


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # Позиция слова по счёту
    print(finder2.count('teXT'))  # Количество вхождений слова в тексте
