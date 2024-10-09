# Домашнее задание по теме "Режимы открытия файлов"
# Задача "Учёт товаров"

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''  # Если файл не найден, возвращаем пустую строку

    def add(self, *products):
        existing_products = self.get_products().strip().split('\n') if self.get_products() else []
        existing_names = {product.split(', ')[0] for product in existing_products}

        for product in products:
            if product.name in existing_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(f'{str(product)}\n')

# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Пример для второго запуска
s2 = Shop()
p4 = Product('Potato', 50.5, 'Vegetables')
p5 = Product('Spaghetti', 3.4, 'Groceries')
p6 = Product('Potato', 5.5, 'Vegetables')

s2.add(p4, p5, p6)
print(s2.get_products())