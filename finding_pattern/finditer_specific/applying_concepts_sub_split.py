import re

urls = """
hello
2020-05-20
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""

# only looking for URL's, we have an http, we have an https, sometimes we have a www. sometimes not
# So here we have http:// [that is common amongst all the urls, so that will stay]
# the (s) for http(s) is optional, so we put a ? after the s to say its optional.
# when it comes to the www, some of the urls have it some don't so we have to wrap the www. in a group, so that the ?
# refers to the whole expression in that group, so now the whole expression (www.) is optional.
# then we have a set lowercase, uppercase letters + (cause there could be 1 + times it appears (group)
# then the \. which is an actual dot that is common amongst the websites
# and then another set [lowercase, uppercase letters) for .com/.org/etc and + (1 + times it can appear), group

pattern = re.compile(r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
matches = pattern.finditer(urls)
for match in matches:
    print(match)

subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)

# the \2 & \3 refers to the group number
