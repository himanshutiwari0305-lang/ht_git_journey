name = "Himanshu" # variable declaration of character string
age = 44 # variable declaration of integer
print("Hello, " + name + "! You are " + str(age) + " years old.")

# Type checking
name = "Himanshu"
salary = 161000
is_manager = False
bonus = None

#print(type(name))        # <class 'str'>
#print(type(salary))       # <class 'int'>
#print(type(is_manager))   # <class 'bool'>
#print(type(bonus))        # <class 'NoneType'>

#Relational Operators
a = 10
b = 20
print(a < b)  # True
print(a > b)  # False
print(a == b) # False
print(a != b) # True
###################################################
x = 10
y = 20

# This evaluates to False, but x is still 10 and y is still 20
result = (x > y) 

print(result) # Prints: False
print(type(result)) # Prints: <class 'bool'>
print(x) # Prints: 10 (x did not change into a boolean!)
##############################
print("Trick question: What is the result of this code?")
a = 10
b = 20

result = a > b
result = result + 5
#Python internally converts the boolean to an integer (False becomes 0, True becomes 1) when performing arithmetic operations. So, in this case, False is treated as 0, and the expression evaluates to 0 + 5, which equals 5.

print(result)
print(type(result))

