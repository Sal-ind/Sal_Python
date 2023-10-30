print("#REGULAR EXPRESSION#")
import re
s = "This is a python program portal"
match = re.search("portal",s)
print("Start index",
      match.start())
print("End index",
      match.end())
print(match)
