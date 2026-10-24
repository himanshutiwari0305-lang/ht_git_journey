import pandas as pd
names = ["Himanshu", "Reyansh", "Shreyas"]
#Creating Series from list
series = pd.Series(names) # pd.Series() is a constructor of Series class. It is used to create a Series object. It takes a list as an argument and returns a Series object. The list can be of any data type. The index of the Series is automatically generated starting from 0. The index can also be specified by passing a list of index values as an argument to the pd.Series() constructor.
print(series)
# Output: 0    Himanshu
#         1    Reyansh
#         2     Shreyas
#         dtype: object

# What is 0 1 2 in the output of series? 
# Answer: 0,1,2 are index of series. Index is used to access the value in series if dont specify index.
# Instead of default index we can also specify our own index in series.
# below is an example of series with custom index.
salary = pd.Series([2500000,1800000,1500000],
    index=[101,102,103]
)

print(salary)
#Output: 101    2500000
#102    1800000
#103    1500000
#dtype: int64
print(salary[101])
# Output: 2500000


