import re

text = "Contact me on 123-456-7890 or email me at john.doe@example.com. You can also contact me on my personal email that is jane.smith@company.org"
digit = re.findall(r"\d+", text)
d = re.search(r"\d+", text)
email= re.findall(r"[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print (digit)
print (email)
if d:
    print(d.group())
    
# new = re.sub(r"\d", "X", text)
# print(new)