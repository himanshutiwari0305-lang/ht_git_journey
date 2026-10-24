employees = [
    ['Name', 'Age'],
    ['Amit', 30],
    ['', 28],            # Missing name, we can use either '' or None
    ['Raj'],             # Only name, missing age
    ['Sita', 32],
    ['Ravi', 25],
    ['Neha', ''],
    ['Meena', '30'],     # Age as string
    ['Sameer', None]     # Age is None
]

# ✅ Step 1: Clean rows — only keep those with exactly 2 items, name not empty, and age is valid
cleaned = [
    x for x in employees[1:]
    if len(x) == 2 and x[0] and (
        (isinstance(x[1], int)) or (isinstance(x[1], str) and x[1].isdigit())
    )
]

# ✅ Step 2: Convert age to int if it's in string
cleaned = [[x[0], int(x[1])] for x in cleaned]

# ✅ Step 3: Calculate average age
total_age = sum(x[1] for x in cleaned)
count = len(cleaned)
average_age = total_age / count
print("Average Age:", average_age)

# ✅ Step 4: Create new list with age +1
updated = [[x[0], x[1] + 1] for x in cleaned]

# ✅ Step 5: Print names of people whose updated age > 30
print("Log jinki age +1 ke baad 30 se zyada hai:")
for x in updated:
    if x[1] > 30:
        print(x[0])
