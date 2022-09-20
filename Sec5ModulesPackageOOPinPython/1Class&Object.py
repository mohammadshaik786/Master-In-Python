# A class is a collection of objects
# A Object is an instance of a class

class Vehicle:
    '''def __init__(self,brand,color):
        vehicle_brand = brand
        vehicle_color = color'''
    # It throws that "'Vehicle' object has no attribute 'vehicle_brand'"
    # Constructor Method
    def __init__(self, brand, color):
        self.vehicle_brand = brand
        self.vehicle_color = color

car1 = Vehicle("Toyota", "white")
car2 = Vehicle("Camri","black")

print(car1.vehicle_brand)
print(car2)
print(type(car1))