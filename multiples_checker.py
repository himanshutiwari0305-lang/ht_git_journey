user_number=int(input("Enter a number "))
x=range(1,101)
for i in x:
    if i%user_number==0:
        print(i,"-->It is a multiple of ",user_number)
