import os

for dirpath,dirnames,filenames in os.walk("/Users/mohammadshaik/Desktop"):
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    # print("-----------------")
    pass

# print(os.environ.get("HOME")+ "/" +"myfile.txt")

print(os.path.join(os.environ.get("HOME")+ "/" +"myfile.txt"))

# Get the basename i.e just the filename in the dir
print(os.path.basename("/Users/mohammadshaik/myfile.txt"))

# Get the dir name only, not the file
print(os.path.dirname("/Users/mohammadshaik/myfile.txt"))

# Will give dir name and filename in tuple
print(os.path.split("/Users/mohammadshaik/myfile.txt"))

# check if the path exists on a computer
print(os.path.exists("/Users/mohammadshaik/myfile.txt"))

# used to check if the file exists in the specified path
os.path.isfile("/Users/mohammadshaik/myfile.txt")

# used to check if the dir exists in the specified path
os.path.isdir("/Users/mohammadshaik/myfile.txt")

# Get the fielpath and file with extension in tuple
print(os.path.splitext("/Users/mohammadshaik/myfile.txt"))





