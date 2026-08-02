# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
    
#     file.write("Hello world")
#     file.writelines(["Alice","Bob","Cherry"])
    
# #Using "with" helps to ensures that at the end operations or 
# #when operation are done, files are automatically closed.

try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")