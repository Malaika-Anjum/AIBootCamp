#Write a program to count the number of vowels in a string

def vow_count (text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count=count+1
    return count
        
input_text= input("Enter Text : ")
print(vow_count(input_text))
    