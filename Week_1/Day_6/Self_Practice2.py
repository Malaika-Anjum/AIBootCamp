#Create a program that counts the number of occurrences of a specific word in a text file

def word_count (Sample):
    with open (Sample, "r") as wc:
        lines = wc.readlines()
        count= 0
        word = input("Enter the word to count: ")
        for line in lines:
            count += line.lower().split().count(word.lower())
    print(f"The word '{word}' appears {count} times in the file.")
    
word_count("sample.txt")