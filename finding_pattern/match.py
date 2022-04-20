# Match looks for patterns at the beginning of our string
import re

test_string = '123abc456789abc123ABC'
# We want to search for the pattern 'abc'

pattern = re.compile(r"abc")
match = pattern.match(test_string)
print(match)

new_pattern = re.compile(r"123")
new_match = new_pattern.match(test_string)
print(new_match)