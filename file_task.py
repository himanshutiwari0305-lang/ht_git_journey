name = input("Enter your name: ")
city = input("Enter your city: ")

with open("info.txt", "a") as file:
    file.write("This will be the second line at the end \n")

with open("info.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)
