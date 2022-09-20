# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.
After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.
"""


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __init__(self):
    #   print("Constructed created")

    def move(self):
        pass

    def eat(self):
        print("Animal Eating")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print("Dog walks")


class Fish(Animal):
    def __init__(self, fish_name, fish_age):
        super().__init__(fish_name, fish_age)
        # Animal.__init__(self)
        # self.name = fish_name
        # self.age = fish_age

    def move(self):
        print("Fish swimms")


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print("Bird flies")


dog = Dog("puppy", 10)
dog.eat()
dog.move()

fish = Fish("Nemo", 5)
fish.eat()
fish.move()

bird = Bird("cucu", 9)
bird.eat()
bird.move()
