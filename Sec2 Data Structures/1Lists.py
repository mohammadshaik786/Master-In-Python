"""Lists are mutable"""

myList = [1,2,3,4,5]
# Removes last element by default
myList.pop()
print(myList)

myList.pop(0)
print(myList)

# Append takes only one argument
myList.append(6)
print(myList)

# Merge two lists
myList2 = [7,8]
List = myList + myList2
print(List)

# Appened List into other List
myList2 = [7,8]
myList.append(myList2)
print(myList)

# Replaces item at index
myList[0] = ['Good','Bad']
print(myList)

myList3 = [2,3,1,5,4]
myList3.sort()
myList3.reverse()
print(myList3)

myList4 = ['s','d','a','e','z']
myList4.sort()
print(myList4[-1])

# Accessing nested elements in the list
myList5 = [1,2,3,'a','b','c','c',['Apple','Banana','Orange']]
fruit = myList5[7][2]
ind = myList5.index('c')
cnt = myList5.count('c')
print(fruit,ind,cnt)
