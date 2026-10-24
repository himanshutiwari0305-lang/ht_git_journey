# Basic function — no return value
def greet(name):#def is the keyword to define a function in python, greet is the name of the function and name is the parameter of the function.
    print(f"Hello, {name}")

greet("Priya")   # Hello, Priya

# Function with return
def calculate_tax(salary, rate):
    return salary * rate / 100

tax = calculate_tax(85000, 30)
print(tax)        # 25500.0

#Default Arguments
def greet(name,country='India'):#country is the default argument and if we dont pass any value the for country arguemnt will take default value as India
    print(f'Hello,{name} is from {country}')

greet("Himanshu")
greet('Reyansh','usa')

# Function with List as an argument
def greet_users(names_list):
    """Prints a greeting for every user in the list."""
    for name in names_list:
        print(f"Hello, {name}!")

# Creating the list
players = ["Alice", "Bob", "Charlie"]

# Passing the list into the function
greet_users(players)

# *args allows you to pass a variable number of arguments to a function.
def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

#*args with normal argument
def arg_employee(name, *skills):
    print("Name:", name)
    print("Skills:", skills)

    
arg_employee('Himanshu','python','oralce','postgresql') 

def demo(a, b=100, *args):
    print(a)
    print(b)
    print(args)

demo(10, 20, 30, 40)

#passing the list as an argument to the function with *args
def demo(*args):
    print(args)

numbers = [10, 20, 30]

demo(numbers)
#output ([10, 20, 30],)

#Tuple has one element
#That one element is the entire list.

demo(*numbers)#this is unpacking example where instead of returning one list as a tuple it will return each element of the list as a tuple.
#output (10, 20, 30)

def demo(a, *args):
    print(a)
    print(args)

demo(*[10, 20], 30, 40)

# **kwargs Example
def employee(**kwargs):
    print(kwargs)

employee(
    name="Himanshu",
    age=45,
    city="Noida"
)

def demo(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

demo(
    10,
    20,
    30,
    name="Himanshu",
    city="Noida"
)

###############lamda function###############
# Lambda functions are anonymous functions(a function without a name) in Python, defined using the `lambda` keyword. 
# They can take any number of arguments but can only have one expression. 
# The expression is evaluated and returned.
# lamda Syntax:
# lambda arguments: expression
# here lambda is the keyword to define a lambda function, 
# arguments: Inputs passed into the function (can take zero, one, or multiple arguments).
# expression: A single line of code evaluated and automatically returned (you do not write the return keyword).

# Lambda example to add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Multiple arguments example
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # Output: 24

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep items where x % 2 == 0 evaluates to True
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6, 8]

salaries = [50000, 60000, 75000]

# Add a 10% hike to every salary
updated_salaries = list(map(lambda s: s * 1.10, salaries)) #here map() applies the lambda function to each element of the salaries list, effectively calculating a 10% increase for each salary. The result is then converted back into a list using list().

print(updated_salaries)  # Output: [55000.0, 66000.0, 82500.0]

