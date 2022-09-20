""" 'list' object does support item assignment i.e lists are mutable """
myList = [1,2,3]
myList[2] = 'Apple'
print(myList)

""" 'tuple' object does not support item assignment i.e tuples are immutable """
# myTuple = (1,2,3)
# myTuple[2] = 'Apple'
# print(myTuple)

myTuple = (1,2,3,'a','b','c',[1,2,3])
ele = myTuple[6][0]
print(ele)

myTuple[6][2] = 'Data'
print(myTuple)