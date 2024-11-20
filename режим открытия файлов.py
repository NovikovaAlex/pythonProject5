from pprint import pprint
from tkinter.font import names


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open('products.txt', 'r')
        pprint(file.read())
        file.close()
        return

    def add(self, *products):
        for products in 'products.txt':
            if products.name not in 'products.txt':
                file = open('products.txt', 'a')
                file.write ('*products\n')
                file.close()
            else:
                return f'Продукт { self.name} уже есть в магазине'




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())