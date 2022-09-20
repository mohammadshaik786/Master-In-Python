
# *args and **kwargs in Python

"""def mysum(a,b,c,d):
    return a + b + c + d

result = mysum(1,2,3,4)
print(result)"""

# To make dynamic(generic) the above stmts, By using *args function
def mysum(*args):
    return sum(args)

result = mysum(1,2,3,4,4,5,6,6,4,5)
print(result)

# For dictionary, we can use keyword arguments as **kwargs
def key_val(**kwargs):
    print(kwargs)
    print(kwargs.keys(),  kwargs.values())
    print(kwargs.get("Name"),kwargs.get("Adress"))
    print(kwargs["Name"])

key_val(Name='Mohammad', Age=24, Weight=65)


"""The naming convention for args is *args.It is constant
But for keyword arguments,it varises i.e **name,**keys"""
