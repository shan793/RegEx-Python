import re

my_string = """
hello world
1223
2022-04-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""
# Extract only the names, and the whole name
# Mr. \. to find the dot ? to make it optional, \s for whitespace \w (for word characters, + 1+ times displayed
pattern = re.compile(r"Mr\.?\s\w+")
matches = pattern.finditer(my_string)

for match in matches:
    print(match)
print("_____________________________________________")
# when conditions are useful, we might have Mr. or Mrs or Ms
p = re.compile(r"(Mr|Ms|Mrs)\.?\s\w+")
ma = p.finditer(my_string)

for m in ma:
    print(m)