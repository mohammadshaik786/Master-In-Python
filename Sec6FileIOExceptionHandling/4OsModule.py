import os

print(os.getcwd())

# Change current working directory
print((os.chdir("/Users/mohammadshaik/Desktop")))

# Get current working dierectory
print(os.getcwd())

# Get list of directories
print(os.listdir())

# Cretae new directory
'''if "myFolder" not in os.listdir():
    os.mkdir("myFolder")'''

if "myFolder" not in os.listdir():
    os.makedirs("myFolder/subdir/datafolder")

'''Create file in new dir :
open terminal, follow cmds
(1) cd path
(2) vi filename -> :wq close'''

# Delete specific file
# os.remove("myFolder/subdir/datafolder/newFile.txt")

# Delete specific directory
os.rmdir("myFolder/subdir/datafolder")

# This is dangerous. Removes entire directories
# os.removedirs("myFolder/subdir/datafolder")

os.rename("newFile.txt","newText.txt")


