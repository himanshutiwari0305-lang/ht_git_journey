v_str1="Understanding Python Strings."
v_str2='String can also be declare with single quotes in Python.'
v_str3="""Triple quotes can be used for multi-line strings in Python.
This is useful for docstrings or when you want to include line breaks in 
your string."""
v_str4='Himanshu'
v_str5='Tiwari'
print('We can concatenate strings using the + operator: ' + v_str4 +" " +v_str5)
print("We can calculate the length of a string using the len() function: " + str(len(v_str1)))

#Indexing Example
message = "Himanshu Tiwari"

# Accessing elements
print(message[0])  # Output: H
print(message[2])  # Output: m
print(message[5])  # Output: s

# Slicing Example
print(message[0:8])  # Output: Himanshu
print(message[:8])   # Output: Himanshu
print(message[1:8])  # Output: imanshu
print(message[:len(message)])   # Output: Himanshu Tiwari

print("find gives the index of the first occurrence of the specified value: " + str(message.find('s')))

#v_name=input("Enter your name: ")
#print ("Name length is " + str(len(v_name)))

v_experiences = 15
print("Name is: " + message + " and experience is: " + str(v_experiences) + " years.")
#above statement can also be written using f-string for better readability
print(f"Name is: {message} and experience is: {v_experiences} years.")
#With f-strings, no conversion needed at all like we did above with str(v_experiences). 
#Python converts whatever's inside {} to a string automatically — int, float, list, even a function call result.

###################SPLIT##############################################

###################LIST##############################################
#List of string methods: https://www.w3schools.com/python/python_ref_string.asp
# A list of integers
numbers = [10, 20, 30, 40]
print(f"Numbers List: {numbers}")
# A list of mixed data types
mixed_list = ["Python", 3.14, True, 42]
print(f"Mixed List: {mixed_list}")
print(f"First element of Mixed List: {mixed_list[0]}")
# An empty list
empty = []

print(f"negative indexing Mixed List: {mixed_list[-1]}")
#List can be mutable, which means you can change their content without changing their identity.
numbers[0] = 15
print(f"Updated Numbers List: {numbers}")

###################LIST Comprehension IMPORTANT##############################################
employees = ["himanshu", "ravi", "neha", "amit", "priya"]

# uppercase all names
upper_names = [name.upper() for name in employees]
print(upper_names)
# ['HIMANSHU', 'RAVI', 'NEHA', 'AMIT', 'PRIYA']

# get length of each name
name_lengths = [len(name) for name in employees]
print(name_lengths)
# [8, 4, 4, 4, 5]

# add a domain to each name to build email IDs
emails = [name + "@company.com" for name in employees]
print(emails)
# ['himanshu@company.com', 'ravi@company.com', ...]

#zip() function is used to combine two or more lists into a single iterable object. 
# It pairs elements from each list based on their index, creating tuples. 
# The resulting object can be converted into a list or other data structures for further processing.
employees = ["Himanshu", "Ravi",  "Neha",  "Amit",   "Priya"]
salaries  = [85000,      92000,   78000,   105000,   88000]
depts     = ["IT",       "HR",    "IT",    "Finance", "IT"]

# pair them up
pairs = list(zip(employees, salaries))
print(pairs)


