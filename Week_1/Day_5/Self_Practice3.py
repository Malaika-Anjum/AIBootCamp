#Write a program to reverse the words in a sentence (not the letters)

import re

def reverse_words(text):
    temp = re.findall(r"[a-zA-Z]+", text)   
    temp=temp[::-1]
    temp1 = " ".join(temp) 
    return temp1

text = input("Enter Text : ")
print(reverse_words(text))