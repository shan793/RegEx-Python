import re

test_string = '123abc456789abc123ABC'
# . is all characters
# If we want to actually search for a (.) in our compile method we would have to \ before the .
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
print("----------------------------------------")

test_string2 = 'hello 123_ heyho hohey'

p = re.compile(r"\bhello") # d is digit, D is non digit, s is whitespace, S is non whitespace, w alphanumeric,
# W, non alphanumeric, b beginning of a block that follows whitespace B word that is not at the beginning
m = p.finditer(test_string2)

for ma in m:
    print(ma)
