class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor}')

    def __len__(self):
        return self.number_of_floor

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __it__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        self.number_of_floor += value
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floor }')





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
print(type(h1))
h1 = h1 + 10
print(type(h1))
print(h1)





