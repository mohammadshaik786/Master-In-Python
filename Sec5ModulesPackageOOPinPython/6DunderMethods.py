class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " age is " + str(self.age)

    def __len__(self):
        return self.age


# The below stmt just prints the location & Memory of class, but when used __str__ function it prints tha attributes
nm = Employee("Mohammad", 24)
print(nm)
# print(str(nm))

print(len(nm))
