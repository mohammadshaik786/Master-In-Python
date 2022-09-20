import os

for dirpath,dirnames,filenames in os.walk("/Users/mohammadshaik/Desktop"):
    print(dirpath)
    print(dirnames)
    print(filenames)
    print("-----------------")