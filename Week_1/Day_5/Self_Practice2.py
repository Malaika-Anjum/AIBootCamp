#Create a program to find and replace all email addresses in a text using regex
import re

text = "You can contact by my business email john.doe@gmail.com or you can also contact me using my personel email james.doe@email.com."
email = re.findall(r"[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(email)

replace_email= re.sub (r"[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}","X" , text)
print(replace_email)     