'''Inheritance : Creating new class from already existed class
Parent or Base Class
Child or sub class'''
# Polymorphism : Having many forms (simply Overloading the same method in inherited classes, but the behaviour or action is different)

class Vehicle:
    # the engine is class attribute where each instance(obj) has a constant attribute
    # The engine should outside of the class specification
    engine = "v6"

    vehicle_counter = 0
    def __init__(self, brand, color):
        self.vehicle_brand = brand
        self.vehicle_color = color
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        return self.vehicle_counter

    def drive(self):
        print("Vehicle Driving")


# This class is called in Venv folder

class Truck(Vehicle):
    #Method Overriding
    def drive(self):
        print("Truck Driving")

class MotorVehicle(Vehicle):
    def drive(self):
        print("Motor drive")