#First tuple Example
#fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

#(green, yellow, *red) = fruits

#print(green)
#print(yellow)
#print(red)

#Second code
#employee=("Himanshu","Noida",42)
#(name,city,age)=employee
#print(name)
#print(city)
#print(age)
#if city!="delhi":
#    print("Not in delhi")
#else:
#    print("In delhi")

#Third code
#employee=("Himanshu",("Noida", "Uttar Pradesh"),42) ##Example of nested tuple ("Noida", "Uttar Pradesh")
#(name,city,age)=employee
#print(name)
#print(city)
#print(age)
#if city!="delhi":
#    print("Not in delhi")
#else:
#    print("In delhi")

#Fourth Code
employees = (
    ('Himanshu', 42, 'Noida'),
    ('Neha', 30, 'Delhi'),
    ('Amit', 35, 'Gurgaon')
)
for emp in employees:
    print(emp)  # Each emp is a tuple
    print(employees[0])      # ('Himanshu', 42, 'Noida')
    print(employees[2][0])

