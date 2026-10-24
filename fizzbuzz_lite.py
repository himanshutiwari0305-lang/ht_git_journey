user_number=int(input("Enter a number "))
x=range(1,user_number)
for i in x:
    if i%3==0 and i%5==0:
        print(i,"-->BuzzFizz ")
    elif i%3==0:
        print(i,"-->Fizz ")
    elif i%5==0:
        print(i,"-->Buzz ")
    else:
        print(i)