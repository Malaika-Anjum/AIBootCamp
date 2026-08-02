 sentence = input("Enter a Sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize Dictionary
word_count = {}

# Count word frequence
for word in words:
    word = word.lower()
    
    #because the user might have entered the same word. 
    # ​For example, ​I can say ​uh ​AI in capital or ai in small
    # couple of times and then it would ​take them as two 
    # different words. ​So I'm converting to lowercase for case 
    # insensitivity here. 
    
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)