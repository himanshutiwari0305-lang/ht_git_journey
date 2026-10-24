# Sorting: is the process of arranging DataFrame rows in ascending or descending order based on one or more 
# columns.
import pandas as pd

employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105, 106, 107],
    "name"  : ["Himanshu", "Ravi", "Neha", "Amit", "Priya", "Sona", "Karan"],
    "dept"  : ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance"],
    "salary": [85000, 92000, 78000, 105000, 88000, 67000, 95000],
    "exp"   : [8, 5, 6, 12, 4, 3, 9],
    "city"  : ["Delhi", "Mumbai", "Delhi", "Bangalore", "Delhi", "Mumbai", "Bangalore"]
})

departments = pd.DataFrame({
    "dept"   : ["IT", "HR", "Finance", "Operations"],
    "manager": ["Rajesh", "Sunita", "Vikram", "Anita"],
    "budget" : [500000, 300000, 800000, 400000]
})

# sort by single column — ascending (default)
print(employees.sort_values("salary"))
#    emp_id      name     dept  salary  exp       city
# 5     106      Sona       HR   67000    3     Mumbai
# 2     103      Neha       IT   78000    6      Delhi
# 0     101  Himanshu       IT   85000    8      Delhi
# 4     105     Priya       IT   88000    4      Delhi
# 1     102      Ravi       HR   92000    5     Mumbai
# 6     107     Karan  Finance   95000    9  Bangalore
# 3     104      Amit  Finance  105000   12  Bangalore

# descending
print(employees.sort_values("salary", ascending=False))
#    emp_id  name     dept  salary  exp       city
# 3     104  Amit  Finance  105000   12  Bangalore
# 6     107 Karan  Finance   95000    9  Bangalore
# ...

# sort by multiple columns — dept ascending, salary descending within dept
print(employees.sort_values(["dept", "salary"], ascending=[True, False]))
#    emp_id      name     dept  salary  exp       city
# 6     107     Karan  Finance  105000   12  Bangalore  ← Finance sorted salary desc
# 3     104      Amit  Finance   95000    9  Bangalore
# 1     102      Ravi       HR   92000    5     Mumbai  ← HR sorted salary desc
# 5     106      Sona       HR   67000    3     Mumbai
# 0     101  Himanshu       IT   88000    8      Delhi  ← IT sorted salary desc
# 4     105     Priya       IT   85000    4      Delhi
# 2     103      Neha       IT   78000    6      Delhi

# nlargest / nsmallest — top N rows by a column
print(employees.nlargest(3, "salary"))
#    emp_id  name     dept  salary  exp       city
# 3     104  Amit  Finance  105000   12  Bangalore
# 6     107 Karan  Finance   95000    9  Bangalore
# 1     102  Ravi       HR   92000    5     Mumbai

print(employees.nsmallest(2, "salary"))
#    emp_id  name dept  salary  exp    city
# 5     106  Sona   HR   67000    3  Mumbai
# 2     103  Neha   IT   78000    6   Delhi

# reset_index — resets row numbers after sort/filter
sorted_df = employees.sort_values("salary", ascending=False).reset_index(drop=True)
print(sorted_df.head(3))
#   emp_id  name     dept  salary  exp       city
# 0    104  Amit  Finance  105000   12  Bangalore  ← index starts from 0 again
# 1    107 Karan  Finance   95000    9  Bangalore
# 2    102  Ravi       HR   92000    5     Mumbai