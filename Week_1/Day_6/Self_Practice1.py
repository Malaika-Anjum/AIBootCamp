#Write a program to copy the contents of one file to another

def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dst:
            dst.write(src.read())
        print("File copied successfully!")
    except FileNotFoundError:
        print(f"File '{source}' does not exist.")

source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")

copy_file(source, destination)

##############################################

#Alternative code that I wrote but it's too long and messy but it works perfectly

# def file_to_be_copied(Source):
#     try:
#         with open (Source, "r") as src:
#             stuffs = src.readlines()
#             for stuff in stuffs:
#                 print(stuff.strip())   
#         return stuffs     
#     except FileNotFoundError:
#         print(f"File {Source} doesn't exit")
        
# def copy_of_file(destination, stuffs):
#     with open (destination, "w") as dst:
#             dst.writelines(stuffs)
            
        
# Source = input("Enter the name of the file to be copied: ")

# stuffs = file_to_be_copied(Source)
# if stuffs is not None:
#     destination = input("Enter the name of the destination file: ")
#     copy_of_file(destination, stuffs)