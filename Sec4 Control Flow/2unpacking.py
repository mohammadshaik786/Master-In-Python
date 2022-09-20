# Looping and Unpacking with Dictionaries and Tuples

employees = {"Mohammad":25000, "Suraj" : 50000, "Yaseen" : 30000}

# By default it prints key objects
for person in employees:
    print(person)
    
print("\n\n\n------------------------------------------------------------\n\n\n")

# Prints each object in form of tuple
for item in employees.items():
    print(item)

for key in employees.keys():
    print(key)
for value in employees.values():
    print(value)

for (key,value) in employees.items():
    print(key)
    print(value)

print("\n\n\n------------------------------------------------------------\n\n\n")

# items() method only supports in dictionary 
employees = [("Mohammad", 25000),("Suraj",50000),("Yaseen",30000)]
for (name,sal) in employees:
    print(name,sal)