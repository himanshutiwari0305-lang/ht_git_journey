user_number=int(input("Enter a number "))
x=range(1,user_number+1)
even_counter=0
odd_counter=0
for i in x:
    if i%2==0:
        print(i,"is Even")
        even_counter+=1
    else:
        print(i,"is Odd")
        odd_counter+=1
print("Total Even Count is",even_counter)
print("Total Odd Count is",odd_counter)