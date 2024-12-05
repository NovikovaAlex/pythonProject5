import math

class Figure:
    sides_count = 0


    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = color
        self.filled = True

        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and isinstance(r, int) and isinstance(g, int) and isinstance(b, int)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def  __is_valid_sides(self, *sides):
        if self.__sides % 2 == 0 and isinstance(self.__sides, int) and len(self.__sides) == self.sides_count:
            return True
        else:
            self.__sides = 1
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def  set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
             self.__sides = list(new_sides)
        else:
            return self.get_sides()

class Circle(Figure):
    sides_count = 1

    def __init__(self,color, *sides):
        super().__init__(color, *sides)
        self.__radius = 15/(2*math.pi)

    def get_square(self):
        print(self.__radius)
        return math.pi*self.__radius**2

class Triangle(Figure):
    sides_count = 3

    def __init__(self,color, *sides):
        super().__init__(color, *sides)


    def get_square(self):
        a, b, c = self.__sides
        p = 0.5 * (a + b + c)
        s = math.sqrt(p*(p -a)*(p - b)*(p - c))
        return s

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, side_length)
        self.__sides = [side_length] * self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], (int, float)) and new_sides[0] > 0:
            self.__sides = [new_sides[0]] * self.sides_count


    def get_volume(self):
        v = self.__sides[0]**3
        return v



circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())











