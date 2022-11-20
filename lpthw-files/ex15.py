# This import the argument variable module into the program
from sys import argv
# This line breaks the argument variable up into two pieces
# The first piece being the imported script and the second being variable flown in
script, filename = argv

# Storing the file into a varible/object
txt = open(filename)

# Printing out the name of the file
print(f"Here's your file {filename}:")
# Adding a function to the txt variable so the file can be read
# Print the text read from the file
print(txt.read())
txt.close()
#
# # Let's double check our steps
# file_again = input("Type the filename again:")
# # Repeat the open file step
# txt_again = open(file_again)
# # Repeat the read file step
# print(txt_again.read())
