# Search method searches through the string and finds any location where it finds matches

import re

test_string = '123abc456789abc123ABC'
# We want to search for the pattern 'abc'

pattern = re.compile(r"abc")
match = pattern.search(test_string)
print(match)

# Will return the first match object