class Animal:
    alive = True
    fed = False

    def __init__(self,name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        self.food = Plant
        print(f'{self.name} съел {food.name}')
        self.alive = True
        self.fed = True

class Predator(Animal):
    def eat(self, food):
        self.food = Plant
        print(f'{self.name} не стал есть {food.name}')
        if self.food == Plant:
            self.alive = False

class Plant:
    edible = False
    def __init__(self,name):
        self.name = name

class Fruit(Plant):
    edible = True

class Flower(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)