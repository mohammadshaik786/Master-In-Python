# print("My First Name is {0}, Last Name is {1} and Middle Name is {2}".format('Mohammad','Shaikh','Suleiman'))

# name = 'Mohammad Shaik'
# # name[9:] = 'Sulaiman'
# name = name[0:8] + ' Sulaiman'
# print(name)

"""original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]

list = list(original_list[3])
list.sort()
res = tuple(list)
original_list[3] = res
print(original_list)"""
from os import name

"""def separate(lst,str):
    return lst + list(str)

print(separate(['a','b','c'],"hello there"))"""

'''def fun(str,**kwargs):
    # lst1 = kwargs.values()
    lst1 = kwargs[key]
    # lst = list(lst1)
    return lst1[-2]
'''
'''res = fun('moh',name = ['M','o'],lname = ['s','k'])
print(res)'''

'''
def pay_extra(work,hour):
    if work or 20 <= hour <= 8:
        print(True)
    elif work or 9<=work<=19:
        print(False)
    else:
        print(False)

pay_extra(False,18)'''



def sequence(numbers):
    for i in range(len(numbers)-2):
        if numbers[i] == 1 and numbers[i+1] ==2 and numbers[i+2] ==3:
            # print(numbers[i])
            # print(True)
            return True
    # print(numbers[i])
    return False

# lists = list(input("Enter sequence:"))
lists = [1,2,3,4,5,6]
print(sequence(lists))

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
#
# num_list = list(input("Enter List:"))
# # num_list = [1,2,3,4,5,6]
# print(sequence,(num_list))


# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False



# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
#
#
# # num_list = list(input("Enter List:"))
# num_list = [1,2,3,4,5,6]
# print(sequence(num_list))


# def first3(my_list):
#     # if my_list[:4].contains(6):
#     # if '6' in my_list[:4]:
#     for i in range(my_list[:4]):
#         if (my_list[i] == '6' or my_list[i+1] == '6' or my_list[i+2] == '6' or my_list[i+3] == '6'):
#             return True
#         return False


def last2(word):
   find_word = word[-2:]



word = 'abcdab'
print(last(word))