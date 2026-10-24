import pandas as pd

employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name"  : ["Himanshu", "Ravi", "Neha", "Amit", "Priya", "Sona", "Karan","Rohit"],
    "dept"  : ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance","Sales"],
    "salary": [85000, 92000, 78000, 105000, 88000, 67000, 95000, 75000],
    "exp"   : [8, 5, 6, 12, 4, 3, 9, 7],
    "city"  : ["Delhi", "Mumbai", "Delhi", "Bangalore", "Delhi", "Mumbai", "Bangalore", "Delhi"]
})

departments = pd.DataFrame({
    "dept"   : ["IT", "HR", "Finance", "Operations"],
    "manager": ["Rajesh", "Sunita", "Vikram", "Anita"],
    "budget" : [500000, 300000, 800000, 400000]
})

print(employees.groupby("city")["salary"].sum()) # Since groupby is a method of DataFrame, In python we call method using () to pass arguments while [] is used to access the column of dataframe. 
# Here we are grouping the dataframe by city and then summing the salary of each city. The output will be a series with city as index and sum of salary as values.
# with above way we can process only one column of dataframe. If we want to process multiple columns of dataframe then we can use agg() method.
# Output:
# city  
# Delhi        251000
# Mumbai       159000
# Bangalore    200000
# Name: salary, dtype: int64

print(employees.groupby("city").agg(total_salary=("salary", "sum"))) # we can also use agg() method to aggregate the data. 
# We can also rename the column name using agg() method. Here we are renaming the column name from salary to total_salary.
# Output:
#             total_salary
# city
# Bangalore        200000
# Delhi           251000                                                                                                    
# Mumbai          159000

result = employees.groupby("dept").agg(
    total_salary  = ("salary", "sum"),
    avg_salary    = ("salary", "mean"),
    max_salary    = ("salary", "max"),
    headcount     = ("emp_id", "count"),
    avg_exp       = ("exp",    "mean")
)
print(result)
#          total_salary   avg_salary  max_salary  headcount    avg_exp
# dept
# Finance        200000  100000.0000      105000          2   10.50000
# HR             159000   79500.0000       92000          2    4.00000
# IT             251000   83666.6667       88000          3    6.00000

# PL/SQL equivalent:
# SELECT dept,
#        SUM(salary)   AS total_salary,
#        AVG(salary)   AS avg_salary,
#        MAX(salary)   AS max_salary,
#        COUNT(emp_id) AS headcount,
#        AVG(exp)      AS avg_exp
# FROM employees
# GROUP BY dept

result = employees.groupby(["dept","city"]).agg(
    avg_salary    = ("salary", "mean"),
    headcount     = ("emp_id", "count")
)
print(result) # example of grouping by multiple columns. Here we are grouping the dataframe by dept and city 
# and then calculating the average salary and headcount of each group.
# Output:   
#                       avg_salary  headcount
# dept    city                               
# Finance Bangalore  100000.000000          2
# HR      Mumbai      79500.000000          2
# IT      Delhi       83666.666667          3

employees["dept_avg_salary"] = employees.groupby("dept")["salary"].transform("mean")
employees["emp_rounded"] = employees["dept_avg_salary"].round() # this add a new column to the employee dataframe 
# which is the rounded value of the average salary of each department. 
# The transform() method is used to return a series with the same index as the original dataframe. 
# The round() method is used to return the rounded value of the series.
print(employees[["name", "dept", "salary", "dept_avg_salary","emp_rounded"]]) 
# Output:
#        name     dept  salary  dept_avg_salary  emp_rounded        
#  0  Himanshu       IT   85000     83666.666667      83667.0
#  1      Ravi       HR   92000     79500.000000      79500.0
#  2      Neha       IT   78000     83666.666667      83667.0
#  3      Amit  Finance  105000    100000.000000     100000.0
#  4     Priya       IT   88000     83666.666667      83667.0
#  5      Sona       HR   67000     79500.000000      79500.0
#  6     Karan  Finance   95000    100000.000000     100000.0 

print(employees)

# agg() summary banata hai; transform() group ka result har original row tak pahunchata hai.

print(departments)
# 3) Merge and Join

# Mental model: merge() is our SQL JOIN. Every JOIN type we know from Oracle maps directly.
result = employees.merge(departments, on="dept", how="inner", indicator=True)
# indicator=True adds a column to the output DataFrame called _merge with information on the source of each row.
print(result)

no_dept = employees.merge(departments, on="dept", how="left", indicator=True)
missing = no_dept[no_dept["_merge"] == "left_only"] # here we are filtering the rows which are present in 
# employees dataframe but not in departments dataframe.
print(missing)
# equivalent to: SELECT * FROM employees e
#                LEFT JOIN departments d ON e.dept = d.dept
#                WHERE d.dept IS NULL

# Vertical Concat Examples
batch1 = pd.DataFrame({
    "Emp_ID": [101, 102],
    "Name": ["Himanshu", "Amit"]
})

batch2 = pd.DataFrame({
    "Emp_ID": [103, 104],
    "Name": ["Rahul", "Neha"]
})

batch3 = pd.DataFrame({
    "Emp_ID": [104, 105],
    "Name": ["Neha", "Raman"]
})

combined = pd.concat([batch1, batch2, batch3], ignore_index=True) 
# here we are concatenating three dataframes batch1, batch2, and batch3. It does not remove duplicates similar to UNION ALL in sql.
print(combined)

# Horizontal Concat Examples
emp_basic = pd.DataFrame({
    "Emp_ID": [101, 102, 103],
    "Name": ["Himanshu", "Amit", "Rahul"]
})

emp_salary = pd.DataFrame({
    "Salary": [2500000, 1800000, 1500000],
    "Bonus": [200000, 100000, 50000]
})

combined = pd.concat(
    [emp_basic, emp_salary],
    axis=1
)

print(combined)
#Output:
#   Emp_ID      Name  Salary   Bonus 
#
# 0    101    Himanshu  2500000    200000
#1    102      Amit  1800000    100000
#2    103     Rahul  1500000     50000

#axis=0 → rows ke direction mein combine.
#axis=1 → columns ke direction mein combine.

# Difference between merge() and concat():
# merge() is used to combine two dataframes based on a common column(s) or index
# concat() is used to combine two dataframes along an axis (rows or columns).