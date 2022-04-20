import re

test_string = '123abc456789abc123ABC'
# We want to search for the pattern 'abc'

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

# Returns match object with the start and the end position
# Regular expression is case sensitive
# r means raw string

# You have three methods to play with match(), search(), findall()
