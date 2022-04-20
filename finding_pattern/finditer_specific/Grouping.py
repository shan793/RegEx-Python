import re
my_string = """
hello world
1223
2022-04-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
Mr. T
"""
# Find all the email address
# So our expression will be a set[lowercase letters, uppercase letters, numbers, or -)]+ (occuring 1 or more times)
# and an @ and another set (for the domain) set[lowercase, uppercase, numbers or -] + (occuring 1 or more times)
# and a actual . \. and then another set with [lowercase letters]
pattern = re.compile(r"[a-zA-Z0-9-]+@[a-zA-Z-]+\.[a-z]+")
matches = pattern.finditer(my_string)

for match in matches:
    print(match)
print("_________________________________________")
# Using groups
p = re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-z]+)")
ma = p.finditer(my_string)

for m in ma:
    print(m.group())
    print(m.group(1)) # name before the @ sign
    print(m.group(2)) # the domain name
    print(m.group(3)) # ending
