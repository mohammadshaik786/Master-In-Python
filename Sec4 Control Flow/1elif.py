# Control Flow: If & Else Statements

# if 2<3 :
if (5<6 and 2<3):
    print("yes")
else:
    print("No")

# Control Flow: Elif Statements

# animal = "ape","Tiger"
# print(animal)
animal = "cow"
if animal == "Monkey":
    print("Eat Bananas")
elif animal == "cow" or animal == "ape" :
    print("Eat Grass")
elif animal == "Lion":
    print("Eat Flesh")
else :
    print("Dont Know what the animal eats")


# For Loops
animals = ["cow","Monkey","ape","Lion","Tiger"]
counter =0

for animal in animals:
    counter = counter + 1
    if animal == "Lion":
        # break
        continue
    sentence = str(counter) + " " + animal  + " lives in jungle"
    print(sentence)

print("loop is terminated")


# Pass Statement in For Loops
# Pass stmt is used for coder to implement logic later if not sure

animals = ["cow","Monkey","ape","Lion","Tiger"]
for animal in animals:
    # Comment to coder ,he can add code later or next week.
    pass

print("Pass stmt is used for coder to implement logic later if not sure")


# While loops

x = 0
while x<10 :
    print(x)
    x=x+1
else:
    print(str(x) +" is not less than 10")

