'''myFile = open(
    "/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/sample")

# The below code reads the file where the cursor starts from 1st word and ends up at last word
content = myFile.read()
print(content)

# if you want the read file again, it doesn't read because the cursor located at last.To overcome this we will set cursor by using seek()

myFile.seek(0)

print("------------------------------")
data = myFile.read()
print(data)

myFile.seek(0)
print("------------------------------")

# To read each line as list, will be using readlines()
# Finally we use close() func to close the file
content_list = myFile.readlines()
myFile.close()
print(content_list)'''

# The above code is like a manual approach where the file need to be closed at last
# The better to be used like 'with' fun

'''with open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/sample") as file:
    new_content = file.read()
print(new_content)'''


'''with open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/sample",mode='a') as file:
    file.write("\nThis is my file")

my_appended_file = open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/sample")
print(my_appended_file.read())'''

# A new file will be created by giving name in path of file like 'sample2'

'''with open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/new_sample",mode='w') as file:
    file.write("\nHello There, Mohammad Here")

my_appended_file = open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/new_sample")
print(my_appended_file.read())'''

# Also the text will be replaced as shown below code

'''with open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/sample",mode='r+') as file:
    file.write("\nHI")

my_appended_file = open("/Users/mohammadshaik/Desktop/Mohammad/TCS/Python/Python_Complete_Course/Sec6FileIOExceptionHandling/sample")
print(my_appended_file.read())'''

# The entire text file can be replaced as below
with open("/Sec6FileIOExceptionHandling/new_sample", mode='w+') as file:
    file.write("\nHI")

my_appended_file = open("/Sec6FileIOExceptionHandling/new_sample")
print(my_appended_file.read())