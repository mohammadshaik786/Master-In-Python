# When u imported re module, u can use reg expressions
import re

txt = "Mohammad is here,hey Mohammad"
x = re.search("^Mohammad.*here$",txt)

if (x):
    print("We had a match")
else :
    print("No match")

y = re.findall("Mohammad",txt)
print(y)
