#Example 1: Read from a Text File
with open("FileHandling/Sample.txt", "w") as file:#with option will close the file automatically
    content=file.write("this the First file I have written in python")
    print(content)#this print the number of characters written in the file.
###########################################################

# Overwriting/Creating a file, if anything is already written in the file, it will overwrite the content of the file.
with open("FileHandling/Sample.txt", "w") as file:
    file.write("I have overwritten in the file.\n")

# Appending to that same file, it does not overwrite the file, it will add the new line to the bottom of the file.
with open("FileHandling/Sample.txt", "a") as file:
    file.write("This line gets added to the bottom!\n")

with open("FileHandling/Sample.txt", "r") as file:#with option will close the file automatically
    content = file.read()
    file.seek(0)  # Move the cursor back to the beginning of the file
    lines = file.readlines() #returns the list of lines in the file
    print(content)
    print(lines)