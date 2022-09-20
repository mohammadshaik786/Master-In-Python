# Exception Handling is handling the programs crash,whenver the program is executed if it throws the error the entire program is crashed
# To Overcome this Exception Handling is used where it points the error and it is handled exception block and interpreter executes the lines of code.

# try block. The code which can throw any exception is kept inside(or enclosed in) a try block. ...
# catch block. catch block is intended to catch the error and handle the exception condition. ...
# Finally block, the code in this block will be executed ireespective of the exception
try:
    with open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/new_sample",mode='r') as my_File:
    # with open("/Sec6FileIOExceptionHandling/new_sample", mode='r') as my_File:
        print(my_File.read())
        sum = 2+'2'
except FileNotFoundError:
    print("There was FileNotFoundError")
except TypeError:
    print("There was TypeError")
except:
    print("Error occured logging to the system")
finally:
    print("The stmt is executed regardless of exception or not")



print("This line should be executed")

# After Catching the exception i.e  after except we can use exact errortype or else like just "except:"