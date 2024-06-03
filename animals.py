class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("chirp")
    def move(self):
        print("the bird is flying")
    def food(self):
        print("seeds")

class Fish(Animal):
    def make_sound(self):
        print("click")

    def environment(self):
        print("water")

    def food(self):
        print("plankton")
    
class Dog(Animal):
    def make_sound(self):
        print("barking")
    def move(self):
        print("start walking")
    def meal(self):
        print("bones")

class Human(Animal):
    def make_sound(self):
        print("Hi,I am a human")
    def move(self):
        print("start walking")
    def eat(self):
        print("I am eating rice")
    def occupation(self):
        print("I am a Doctor")

class Donkey(Animal):
    def make_sound(self):
        print("brays")
    def move(self):
        print("walking")
    def eat(self):
        print("grass")
    def use(self):
        print("I can luggage")