"""
Dictionary is a collection of key-val pairs.
In Lists & Tuple elements are accessed based on index where as in Dic elements are accessed based on keys.
Similar to Lists, Dic are Mutable

 Note: """
people_wt_dict = {'Mohammad' : 65,'Suraj' : 63, 'Yaseen' : 68}
print(people_wt_dict)
print(people_wt_dict['Suraj'])

people_wt_dict['Mohammad']=64
print(people_wt_dict)

# pop expected at least 1 arguments, got 0 unlike in List, last element will be deleted
people_wt_dict.pop('Yaseen')
print(people_wt_dict)

# Appending Key-Val to tuple
people_wt_dict['Yaseen'] = 70
print(people_wt_dict)

people_wt_dict['Items'] = ['Orange','Banana']
print(people_wt_dict)
print(people_wt_dict['Items'][1])

people_wt_dict['Items'] = ['Orange',{'Banana' : 'Yellow'}]
print(people_wt_dict)
print(people_wt_dict['Items'][1]['Banana'])

people_wt_dict.clear()
print(people_wt_dict)


