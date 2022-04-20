import re

dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

# Want to extract dates with the format yyyy-mm-dd and yyyy/mm/dd
# pattern = re.compile(r"\d\d\d\d[-/]\d\d[-/]\d\d")

# looking for months in may and july
# pattern = re.compile(r"\d\d\d\d[-/]0[5-7][-/]\d\d")

#Instead of manually typing out d's we can use a quantifier to select the number of digits
pattern = re.compile(r"\d{4}[-/]0[5-7][-/]\d{2}")
matches = pattern.finditer(dates)
for match in matches:
    print(match)
# If you want to print out the dates instead of returning a match object, use findall and then print to std out
# pattern = re.compile(r"\d{4}[-/]0[5-7][-/]\d{2}")
# matches = pattern.findall(dates)
# print(matches)