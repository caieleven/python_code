import re
li = ["fjei", "jei", "fjefejii"]
s = str(li)
a = "i have an * \    \n[]"
print(a)
x = re.sub(r'[\s\*\[\]]', '',  a)
print(x)
