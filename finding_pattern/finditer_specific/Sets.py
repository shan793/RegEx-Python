import re

test_string = 'helloHELLO 123_ heyho hohey'
# Sets find each instance of each individual character you pass into it, not the block as a whole
# You can specific a-z to find all the letters here, or 0-9 to find all the digits
# Can write ranges back to back
pattern = re.compile(r"[a-zA-Z0-9]")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)