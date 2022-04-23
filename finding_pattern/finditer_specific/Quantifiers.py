import re

test_string = "hello_1_2_3"
# * zero or more, + one or more, combine digits in one match
# ? character to the left of underscore optional, and will return what it can find

pattern = re.compile(r"_?\d")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

print("______________________")

test_string_2 = "hello123"

# Find digits in range 1 - 3
p = re.compile(r"\d{1,3}")
ma = pattern.finditer(test_string_2)

for m in ma:
    print(m)