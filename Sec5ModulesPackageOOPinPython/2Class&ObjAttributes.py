class Vehicle:
    # the engine is class attribute where each instance(obj) has a constant attribute
    # The engine should outside of the class specification
    engine = "v6"  # Simply a static variable

    vehicle_counter = 0

    def __init__(self, brand, color):
        self.vehicle_brand = brand
        self.vehicle_color = color
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        return self.vehicle_counter


# refrain from doing below.
# should not be changing class specification outside of class.
# potentially a bad smell in the code
Vehicle.engine = "v5"

car1 = Vehicle("Toyota", "white")

# The following 2 lines of code are not following a class specification. leads to poor design in long run.
car1.color = "blue"
car1.make = "good"

print(car1.get_vehicle_count())

car2 = Vehicle("Camri", "black")
car3 = Vehicle("Tesla", "red")

print(car2.get_vehicle_count())
print(car3.get_vehicle_count())

print(car1.engine, car2.engine, car3.engine)

print(car1.vehicle_brand)


"""
# Create a utility function as a static method
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")"""