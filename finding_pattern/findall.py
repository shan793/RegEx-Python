import re

test_string = '123abc456789abc123ABC'
# We want to search for the pattern 'abc'

pattern = re.compile(r"abc")
matches = pattern.findall(test_string)

for match in matches:
    print(match)