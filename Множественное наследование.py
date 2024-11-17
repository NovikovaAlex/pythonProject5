import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cord = [0, 0, 0]
        self.speed = speed

    def move (self, dx, dy, dz):
        x = self._cord[0] + dx  * self.speed
        y = self._cord[1] + dy  * self.speed
        z = self._cord[2] + dz * self.speed
        if z <= 0:
            print ("It's too deep, i can't dive:(")
        else:
            self._cord[0] = x
            self._cord[1] = y
            self._cord[2] = z

    def get_cords(self):
        print(f'X: {self._cord[0]}, Y: {self._cord[1]}, Z:{self._cord[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random_number = random.randint(1,4)
        print( f'Here are(is) {random_number} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        change = abs(dz) * self.speed / 2
        z = self._cord[2] - change
        if z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cord[2] = z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird,):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)




db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()



