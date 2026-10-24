# Boolean Indexing — is a powerful data-filtering technique in Pandas that allows you to select rows 
# from a DataFrame based on actual data values rather than row numbers or labels.
# It is like WHERE clause.
# Use square brackets df[...] for filtering
# Always wrap conditions in parentheses (df['Col'] > val) when combining them.

import pandas as pd

data = {
    'Name': ['Himanshu', 'Amit', 'Rahul', 'Priya'],
    'Department': ['IT', 'Finance', 'IT', 'HR'],
    'Salary': [85000, 60000, 90000, 75000]
}

df = pd.DataFrame(data)

# Step 1: See what the condition itself produces
print(df['Salary'] > 75000) # this condition checks every single row in that column and returns a Series of Booleans (True or False).
# Output:
# 0     True
# 1    False
# 2     True
# 3    False
# row 0 and row 2 as True because their salaries are greater than 75,000.

# Step 2: Pass the condition into the DataFrame
high_earners = df[df['Salary'] > 75000]

print(high_earners)
# Output:
#       Name Department  Salary
# 0  Himanshu         IT    85000
# 2    Rahul         IT    90000

# Combining Multiple Conditions (AND / OR)
# In SQL, we use AND and OR keywords. In Pandas Boolean Indexing, you must use bitwise operators:
# Each condition must be in parentheses().

# 1) & (AND) — Both conditions must be True.
# 2) | (OR) — At least one condition must be True.

# AND — both conditions must be true
print(df[(df["Department"] == "IT") & (df["Salary"] > 80000)])
#       Name Department  Salary
# 0  Himanshu         IT    85000
# 4     Priya         IT    88000

# OR — either condition is enough
print(df[(df["Department"] == "Finance") | (df["Salary"] > 90000)])
#       Name Department  Salary
# 1    Ravi         HR    92000
# 3    Amit    Finance   105000

# NOT — use ~ to negate a condition
print(df[~(df["Department"] == "IT")])
#       Name Department  Salary
# 1    Ravi         HR    92000
# 3    Amit    Finance   105000

# Filtering with .isin() — like SQL's IN clause
# WHERE dept IN ('IT', 'HR')
print(df[df["Department"].isin(["IT", "HR"])])
#       Name Department  Salary
# 0  Himanshu         IT    85000
# 1      Ravi         HR    92000
# 2      Neha         IT    78000
# 4     Priya         IT    88000

# Filtering with .between() — like SQL's BETWEEN clause
# WHERE salary BETWEEN 80000 AND 95000
print(df[df["Salary"].between(80000, 95000)])
#       Name Department  Salary
# 0  Himanshu         IT    85000
# 1      Ravi         HR    92000
# 4     Priya         IT    88000

# SQL vs Pandas comparison
# +--------------------------------------------------------+---------------------------------------------------------------+
# | SQL                                                    | Pandas                                                       |
# +--------------------------------------------------------+---------------------------------------------------------------+
# | WHERE Salary > 1800000                                 | df[df["Salary"] > 1800000]                                   |
# | WHERE Salary >= 1800000                                | df[df["Salary"] >= 1800000]                                  |
# | WHERE State = 'UP'                                     | df[df["State"] == "UP"]                                     |
# | WHERE State <> 'UP'                                    | df[df["State"] != "UP"]                                     |
# | WHERE Salary > 1500000 AND State = 'UP'                | df[(df["Salary"] > 1500000) & (df["State"] == "UP")]       |
# | WHERE State = 'UP' OR State = 'Bihar'                  | df[(df["State"] == "UP") | (df["State"] == "Bihar")]      |
# | SELECT Name, Salary ... WHERE State='UP'               | df.loc[df["State"] == "UP", ["Name","Salary"]]            |
# +--------------------------------------------------------+---------------------------------------------------------------+


# query() — reads closest to SQL WHERE
# simple
print(df.query("Department == 'IT' and Salary > 80000"))

# using a Python variable inside query — prefix with @
min_salary = 60000
print(df.query("Salary >= @min_salary and Department != 'HR'"))
#        Name Department  Salary
# 0  Himanshu         IT   85000
# 1      Amit    Finance   60000
# 2     Rahul         IT   90000

# Why use .query() instead of regular Boolean Indexing?
# 1) It is more readable and closer to SQL syntax.
# 2) It can be faster for large DataFrames because it uses numexpr under the hood, 
# which can optimize the evaluation of expressions.
# Use Boolean indexing for simple one‑condition filters; use .query() when readability and complex conditions 
# matter, or when working with very large datasets.