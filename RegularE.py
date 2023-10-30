import re
s="This is A python program Portal"
match=re.search('Portal',s)
print('start index',match.start())
print("End Index",
    match.end())
print(match)
