secret = 7
number = int(input("Enter a number "))
while secret != number:
    if number > secret:
        print("Too high ")
        number = int(input("Enter the number again "))
    elif number < secret:
        print("Too low")
        number = int(input("Enter the number again "))
print("Bingo you guessed it correct")
