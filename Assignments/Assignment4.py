# Assignment 1

"""
Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.
twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True
"""

"""def twelver(a,b):
    if a == 12 or b == 12:
        print(True)
    elif a + b ==12:
        print(True)
    else :
        print(False)"""

"""def twelver(a, b):
  return (a == 12 or b == 12 or a+b == 12)

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
print(twelver(a,b))"""

print("\n\n\n------------------------------------------------------------\n\n\n")

# Assignment 2

"""
Create a method called pay_extra that accepts 2 parameters:
 working, and hour. This method will be used to decide whether
 an employee will receive extra pay or not. If an employee is working
 during the hrs of 8pm until 8am in the morning, that means they
 should be paid extra. In that situation the method should return true,
 otherwise it should return false.
 NOTE: the hour parameter should be from 0-23.
        So 8AM is hour 8, and 8PM is hour 20.
Example:
    pay_extra(True, 11) -> false
    pay_extra(False, 5) -> false
    pay_extra(True, 6)  -> true
"""

"""def pay_extra(working,hour):
    if(working and (hour<=8 or hour>=20)):
        return True
    else:
        return False"""

"""def pay_extra(working,hour):
    return (working and (hour<=8 or hour>=20))

working = bool(input("Enter working:"))
hour = int(input("Enter hours:"))
print(pay_extra(False,hour))"""

"""
def pay_extra(work,hour):
    if work=="True":
        if hour in range(20,25) or hour in range(1,9):
            return True
        else:
            return False
    else:
        return False"""

# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.
sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
#
# num_list = [int(item) for item in input("Enter the items seperated by space:").split()]
# num_list = [1,2,3,4,5,6]
# print(sequence,(num_list))

# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'
"""

# Your Code Below:

'''def grow_string(word):
    res = ""
    # while i < len(word):
    for i in range(len(word)):
        res = res + word[:i+1]
    return res
word = input('Enter a word:')
print(grow_string(word))'''


print("\n\n\n------------------------------------------------------------\n\n\n")

# Assignment 5

"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.
first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False
"""

# Your Code Below:

'''def first3(my_list):
    end = len(my_list)
    if end > 4:
        end = 4
    for i in range(end):
        if my_list[i] == '6':
            return True
    return False


my_list = [1,2,3,4,5,6]
# print(my_list[:4].contains('1'))
print(first3(my_list))'''

"""def first3(num_list):
    if 6 in num_list[0:5]:
        return True
    else:
        return False


List = []
List = [int(item) for item in input("Enter the items seperated by space:").split()]
print(first3(List))"""



print("\n\n\n------------------------------------------------------------\n\n\n")

# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.
So "hixxxhi" yields 1 (we won't count the end substring).
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""

# Your Code Below:

'''def last2(word):
    if len(word)<2:
        return 0
    find_word = word[-2:]
    rest_word = word[:-2]
    cnt=0
    for i in range(len(rest_word)):
        sub = rest_word[i:i+2]
        if sub == find_word :
            cnt+=1
    return cnt

word = 'abxxxxcdbcxx'
print(last2(word))'''

"""def last2(String):
    cnt=0
    if len(String)<2:
        return 0
    for i in range(len(String)-2):
        if String[i:i+2]==String[-2:]:
            cnt= cnt+1
    return cnt


String = input("Eneter the string:")
print(last2(String))"""
print("\n\n\n------------------------------------------------------------\n\n\n")


# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.
EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0
"""

#Your Code Below:

''' 
# another way.... if the substring positions are not in same place
def string_match(word1,word2):
    cnt = 0
    for i in range(len(word1)):
        for j in range(len(word2)):
            sub1 = word1[i:i+2]
            sub2 = word2[j:j+2]

            if sub1 == sub2:
                cnt+= 1
    return cnt

# word1 = input("Enter word1:")
# word2 = input("Enter word2:")
# print(string_match(word1,word2))

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))'''

'''def string_match(word1,word2):
    shorter = min(len(word1),len(word2))
    cnt = 0
    for i in range(shorter-1):
        sub1 = word1[i:i+2]
        sub2 = word2[i:i+2]
        if sub1 == sub2:
            cnt+= 1
    return cnt

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))'''


"""def string_match(str1, str2):
    cnt = 0
    l1, l2 = len(str1), len(str2)
    if l1 <= l2:
        tmp = range(l1-1)
    else:
        tmp = range(l2)
    print(tmp)
    for i in tmp:
        if str1[i:i + 2] == str2[i:i + 2]:
            cnt = cnt + 1
    return cnt"""

print("\n\n\n------------------------------------------------------------\n\n\n")

# Assignment 8

"""
Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.
EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4
"""

# Your Code Below:

'''def sum78(my_list):
    sum = 0
    # j = -1
    ind1 = my_list.index(7)
    ind2 = my_list.index(8)
    new_list = my_list[0:ind1] + my_list[ind2+1:]
    for i in range(len(new_list)):
        sum+=new_list[i]
    return sum

# print(sum78([1, 2, 2]))
print(sum78([1, 2, 2, 7, 99, 99, 8]))
print(sum78([1, 1, 7, 8, 2]))'''



'''def sum78(nums):
    sum = 0
    inRange = False

    for i in range(len(nums)):
        if nums[i] == 7:
            inRange = True

        if not inRange:
            sum += nums[i]

        if inRange and nums[i] == 8:
            inRange = False

    return sum

# print(sum78([1, 2, 2]))
print(sum78([1, 2, 2, 7, 99, 99, 8]))
print(sum78([1, 1, 7, 8, 2]))'''


print("\n\n\n------------------------------------------------------------\n\n\n")


# Assignment 9

'''
We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with
the associated value of that email looked up from the dictionary d.
If the dictionary does not contain the email found in the list, add a new entry
in the dictionary for the email found in the fr list. The value for this new email key
will be the next highest value number in the dictionary in string format.
Once the dictionary is populated with this new email key and a new number value,
replace that email's occurrence in the fr list with the number value.
The output of running your completed code should be the following:
Value of fr:
['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
Value of d:
{'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}
"""

# Don't manually change fr and d.
fr = [
'7@comp1.COM|4|11|GDSPV',
'7@comp1.COM|16|82|GDSPV',
'13@comp1.COM|12|82|GDSPV',
'26@comp1.COM|19|82|GDSPV'
]

d= {
'7@comp1.COM': '199',
'8@comp4.COM': '200',
'13@comp1.COM': '205'
}
'''

# Your Code Below:

print("Value of fr: ")
print(fr)
print("Value of d:")
print(d)

line_list = []
# this won't work for missing keys
for line in fr:
    columns = line.split("|")
    lookup_val = columns[0]

    # if lookup_val not in d.keys():
    if(d.get(lookup_val) is None): # Can't find in dict

        # get the next number + 1 from dict
        next_number = int(max(d.values())) + 1
        d[lookup_val] = str(next_number)
        columns[0] = str(next_number)
        line_list.append("|".join(columns))
    else:
        columns[0] = d.get(columns[0])
        line_list.append("|".join(columns))

fr1 = line_list
print(fr1)