# Without enumerate — PL/SQL style (manual counter)
emps=["Himanshu","Rekha","Reyansh"]
i = 0
for emp in emps:
    print(i, emp)
    print("Without enumerate:")
    i += 1
# With enumerate — Pythonic style
for i,emp in enumerate(emps):
    print(i,emp)
# With enumerate and start parameter
for i,emp in enumerate(emps,start=1):
    print('this is enumerate with start value ', i, emp)

# enumerate() collapses the "maintain a manual counter alongside your loop" pattern. 
# In data engineering you'll use it constantly to add sequence numbers or row positions to records.

#Whie Loop
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1 
# zip() is a buit in function in python that takes iterables, aggregates them in a tuple, and returns it.
names = ["Priya", "Ravi", "Sona"] # this is a list of names
ages = [25, 30, 28] # this is a list of ages

result = zip(names, ages)
print(list(result))

# For loop
students=['Himanshu','Reyansh','Shreyas']
for s in students:
    print(s)

#Another example
v_name='Himanshu'
for v in v_name:
    print(v)

#else in for loop
for s in students:
    print(s)
else:# Executes only if break never happened
    print("All students have been printed.")

#example of break statement
emps = ["Himanshu", "Reyansh", "Shreyas"]

search_emp = "Reyansh"

for emp in emps:
    if emp == search_emp:
        print("Employee Found")
        break
else:
    print("Employee Not Found")

#for loop with pass statement
for i in range(5):
    pass  # Placeholder for future code, pass will do nothing and will not throw any error.

#for loop with continue statement
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop for this iteration
    print(i)