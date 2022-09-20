# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:
"""def merge_lists(list1,list2):
    return list1 + list2

List1 = [1,2,3]
List2 = ['Mohammad','Suraj','Yaseen']
res = merge_lists(List1,List2)
print(res)"""

##############################################################

# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.
    Make sure to test the function.
"""
# Your Code Below:

"""def separate(string):
    # list = string.split()
    return list(string)

print(separate("Mohammad Here"))"""

"""def separate(string):
    for i in string:
        mylist.append(i)

mylist = []
separate("Mohammad Here")
print(mylist)"""

############################################################################

# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.
The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.
"""
# Your Code Below:

"""def multi_merge(List,string):
    return List + string.split() + list(string)

Res = multi_merge([1,2,3],"Mohammad Here")
print(Res)"""

# Dont use list,str as variables 

##################################################################################

# Assignment 4:

"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.
Example:
    For example, the below function call should return ['mike', 'john']
    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])
"""

# Your code below:
"""def last_list(*args):
    # List = list(args)
    # return List[-1]
    # return args[-1]
    return args[-1 :len(args)]

Res = last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])
print(Res)"""

##############################################################################

  
# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.
Example:
    For example, the below function call should return: jan
    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
"""

# Your Code Below:

"""def key_list_items(**newlist):
    # List = newlist.get("people")
    List = list(newlist.values())
    print(List)
    return List[-1][-2]
  

Res = key_list_items( "people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
print(Res)"""

def key_list_items(key,**newlist):
    List = newlist[key]
    print(List)
    return List[-2]
  

Res = key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'],ages=[20, 30, 40])
print(Res)

