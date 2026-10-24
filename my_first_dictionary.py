employee = {
    "name": "Himanshu",
    "name": "Rekha",
    "age": 42,
    "city": "Noida"
}

print(employee["name"])   # Dictionaries cannot have two items with the same key so instead of himanshu it will print rekha:
employee["department"] = "HR"#adding key HR
employee["age"] = 43#change value of age from 42 to 43
#del employee["city"]#delete key city
employee["city"] = "Delhi"# to change city name
print(employee)
for key, value in employee.items():#printing key value using loop
    print(key, ":", value)

print(employee.get("name"))
x = employee.keys()

print(x) #before the change
x = employee.values()
print(x) #before the change
