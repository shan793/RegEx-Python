import re

test_string = '123abc456789abc123ABC'

pattern = re.compile(r"abc")
splitted = pattern.split(test_string)
print(splitted)
# returns a list with the parts that do not contain regex

test_string1 = "hello world, you are the best world"
p = re.compile(r"world")
subbed_string = p.sub("planet", test_string1)
print(subbed_string)
# returns a string