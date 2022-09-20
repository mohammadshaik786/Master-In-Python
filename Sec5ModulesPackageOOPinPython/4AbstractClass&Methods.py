# Abstract class cannot create an instance of class
# Here Animal is an abstract class. Hence Animal class should not be invoked. So to inherit the method eat(), we were invoking that functionality in the next class.
from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self, name):
        self.animalName = name

    @abstractmethod
    def eat(self):
        raise NotImplementedError("Child class should be implementing this")
        # pass


class Monkey(Animal):
    def eat(self):
        print("monkey eating bananas....")


class Bird(Animal):
    def eat(self):
        print("bird eating seeds")

    def fly(self):
        print("Birds fly")


mon = Monkey("piku")
mon.eat()

bird = Bird("pigeon")
bird.eat()
bird.fly()
