# Range, Enumerate, and Zip Functions
# More handy functions & Random Package
# Accepting i/p from user


# Range function

for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

for i in range(2,10,2):
    print(i)

print("\n\n\n------------------------------------------------------------\n\n\n")


# Zip function : Iterator objects that will be joined together for more than 1 list i.e num associated with object
mynum = [1,2,3,4,5]
words = ["HAdoop","Hive","Spark","KAfka","Hbase"]

combinedItems = zip(mynum,words)
print(combinedItems)
for item in combinedItems:
    print(item)

print("\n\n\n------------------------------------------------------------\n\n\n")

# enumerate function- The enumerate() function assigns an index to each item in an iterable object that can be used to reference the item later. ...
# It makes it easier to keep track of the content of an iterable object.
# The defaut index or key takes is 0
combinedItems = enumerate(words)
for item in combinedItems:
    print(item)

# The key can be assigned as another Parameter in function
Items = enumerate(words,10)
for item in Items:
    print(item)

print("\n\n\n------------------------------------------------------------\n\n\n")

# Zip function as list
list_a = [1,2,3,4,5]
list_b = ["Data Engineer","Data Scientist","Data Analyst","BI Developer"]
list_c = ["Python","ML","SQL","PowerBI"]
Roles = list(zip(list_a,list_b,list_c))
print(Roles)
for r in Roles:
    print(r)

for (a,b,c) in Roles:
    print(a)
    print(b)
    print(c)

print("\n\n\n------------------------------------------------------------\n\n\n")

list_a = [1,2,3,4,5]
print(2 in list_a)
dic = {"Mohammad":"Ds","Suraj":"FullStack","YAseen": "Business"}
print("Mohammad" in dic)
print("FullStack" in dic.values())
print(min(list_a),max(list_b))

# For below codes, if executed multiple times, the o/p will be different
from random import randint
print(randint(0,100))

from random import shuffle
shuffle_list = shuffle(list_a)
print(list_a)
shuffle_list = shuffle(list_a)
print(shuffle_list)


name = input("Enter Your Name:")
print("Hello! "+name)

# strip() makes remove the spaces when users enters input i.e "       Mohammad"
name = input("Enter Your Name:")
print("HEllo! "+name.strip())

number = input("Enter the Number: ")
print(10 + int(number))

number = int(input("Enter the Number: "))
print(10 + number)





