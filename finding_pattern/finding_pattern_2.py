import re

test_string = '123abc456789abc123ABC'

# Instead of compiling, we can use find iter to find the matches directly

matches = re.finditer(r"abc", test_string)

for match in matches:
    print(match)