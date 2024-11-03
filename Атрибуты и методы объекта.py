class House():
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor):
        floor = 0
        if new_floor < 1 or new_floor > self.numbers_of_floor:
            print ('Такого этажа не сушествует')
        else:
            for floor in range(new_floor):
                print(floor + 1)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)