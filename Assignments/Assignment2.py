"""
Print Bill's salary from the my_list object shown below.
my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
"""
my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
print(my_list[0]['Bill'])
print(my_list[0].get('Bill'))

# Assignment 2:
"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:
Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""
list = [{'Tom' : {'salary' : 20000,'age' : 22,'items' : ['jacket','car','TV']}},
        {'Mike' : {'salary' : 24000,'age' : 27,'items' : ['bike','laptop','boat']}}]
print(list)

# Assignment 3:
"""
There is a list shown below titled original_list.
Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.
IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.
"""
# Tuple doesn't have sort function
original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]
num1 = original_list[3][0]
num2 = original_list[3][1]
num3 = original_list[3][2]
new_list = [num1,num2,num3]
new_list.sort()
new_tuple = (new_list[0],new_list[1],new_list[2])
print(new_list)
print(new_tuple)
# print(type(original_list[3]) == 'tuple')

"""original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]
list = list(original_list[3])
list.sort()
res = tuple(list)
original_list[3] = res
print(original_list)"""

# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]
my_list[2][0][3] = 'x'
my_list[3] = 'television'
print(my_list)