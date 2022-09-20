# Introduction to Creating Functions

# Note: cntrl+click gives calling fun
# Help Cmd which is used to get info
# help(print)

# No Arguments
def greet_person():
    print("Hello, I'm here!")

greet_person()

# With Parameters
def greet_personArg(name):
    print("Hello," +name+ " here!")
# Called with Argument
greet_personArg('Mohammad')

'''With Parameters having defined.
 Note: Int cannot be concatenated with string, so use int value either in "" or use str() function'''
def greet_personArgdef(name='Mohammad',age=24):
    print("Hello, "+name+" here! with age " +str(age))

# greet_personArgdef('Shaik')
greet_personArgdef()


def greet_personArgdef(name='Mohammad',age=24):
    return "Hello," +name+ " here! with age " +str(age)

person = greet_personArgdef()
print(person)

# rem Function Hands-on
def remainder(num1,num2):
    return num1%num2

print(remainder(10,3))

