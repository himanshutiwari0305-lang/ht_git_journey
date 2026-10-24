import pandas as pd
from pathlib import Path # Adding Pathlib module to handle file paths in a more efficient way. It is a built-in module in Python 3.4 and above. It is used to handle file paths in a more efficient way. It provides an object-oriented interface to the filesystem.

data = {
    "Emp_ID":[101,102,103],
    "Name":["Himanshu","Amit","Rahul"],
    "Salary":[2500000,1800000,1500000],
    "State":["UP","Haryana","Bihar"]
}

# Creating a dataframe. A dataframe is a 2-dimensional(rows and columns) labeled data structure with columns 
# of potentially different types. It is similar to a spreadsheet or SQL table, or a dict of Series objects. 
# It is generally the most commonly used pandas object. DataFrames can be created from various data structures 
# such as lists, dicts, Series, and NumPy arrays.
df = pd.DataFrame(data,index=["E01","E02","E03"])
# pd.DataFrame() is a constructor of DataFrame class. It is used to create a DataFrame object. 
# It takes a dict as an argument and returns a DataFrame object. The dict can be of any data type. 
# The keys of the dict are used as column names and the values of the dict are used as column values. 
# The index of the DataFrame is automatically generated starting from 0. 
# The index can also be specified by passing a list of index values as an argument to the pd.DataFrame() constructor.
print(df)
# Internal representation of dataframe. 
# DataFrame->Series->Emp_ID->Series->Name->Series->Salary
# A DataFrame is actually a collection of Series.

# Accessing one column of dataframe using column name.
print(df["Name"])
# Output:
# 0    Himanshu
# 1       Amit
# 2      Rahul 
# A column of dataframe is actually a series, we can access the value of series using index.

# Accessing multiple columns of dataframe using column name.
print(df[["Emp_ID","Salary"]])  
# Output:
#    Emp_ID   Salary        
#  0  101  2500000
#  1  102  1800000  
#  2  103  1500000
#  Here we are accessing multiple columns of dataframe using column name, the output is also a dataframe.
# 
# Main difference between series and dataframe is that series is
# 
print(df) # Returns whole dataframe   

# DataFrame structure and inspection:
#| Pandas       | Meaning                                                 | SQL / Oracle Equivalent                                                                                   |
#| ------------ | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
#| `df.index`   | Get row indexes                                         | **No direct SELECT equivalent**                                                                           |
#| `df.columns` | Get column names                                        | `SELECT column_name FROM user_tab_columns WHERE table_name = 'EMPLOYEE';`                                 |
#| `df.shape`   | Get `(rows, columns)`                                   | `SELECT COUNT(*) FROM EMPLOYEE;` + `SELECT COUNT(*) FROM user_tab_columns WHERE table_name = 'EMPLOYEE';` |
#| `df.dtypes`  | Get datatype of each column                             | `SELECT column_name, data_type FROM user_tab_columns WHERE table_name = 'EMPLOYEE';`/DESC EMPLOYEE                      |
#| `df.info()`  | Overall DataFrame structure, non-null counts, datatypes | **No single exact SQL query**; conceptually combines metadata + NULL checks                               |
#| `df.head()`  | First 5 rows                                            | `SELECT * FROM EMPLOYEE FETCH FIRST 5 ROWS ONLY;`                                                         |
#| `df.tail()`  | Last 5 rows                                             | `SELECT * FROM EMPLOYEE ORDER BY ... DESC FETCH FIRST 5 ROWS ONLY;`*                                      |

print("loc Label based selection")
# We use loc when we want to select rows and columns by their labels. The following are the different ways to use loc:
# syntax: df.loc[row_labels, column_labels]
#print('loc 1 eg ',df.loc["E01"]) # E01 index ke row ko select karega. ie 101  Himanshu  2500000       UP, so output will :
#Emp_ID         101
#Name      Himanshu
#Salary     2500000
#State           UP

#print('this is ',df.loc[0]) # this will give error since I am using custom index.
print('loc 2 eg ',df.loc["E03", "Name"])# Here "E03" is DataFrame index and Name is column name. It will return the value of Name column for index "E03".    
# output: Rahul
print(df.loc[["E02", "E03"], ["Name", "Salary"]]) #It gives Specific Rows + Columns

print("iloc Position based selection")
print(df.iloc[0]) #It will return the first row of dataframe. iloc is useful when you care about position

# Another way to create a dataframe is by reading a csv file. 
# A csv file is a comma-separated values file. It is a plain text file that contains data in a tabular format. 
# The first line of the file is a header that contains the names of the fields. 
# The rest of the lines are data records. 
csv_path = Path(__file__).resolve().parent / "employees_dummy.csv" # It locates path of current python file
df_csv = pd.read_csv(csv_path) # pd.read_csv() is a function of pandas library. 
print(df_csv) # It will print the whole dataframe. It is similar to df.head() method.


excel_path = pd.read_excel("C:/PythonCode/students_dummy.xlsx") # pd.read_excel() is a function of pandas library. It is used to read an excel file and return a dataframe. It takes the path of the excel file as an argument and returns a dataframe. The excel file can be in .xls or .xlsx format. The first sheet of the excel file is read by default. The sheet name can be specified by passing the sheet name as an argument to the pd.read_excel() function.
print(excel_path.head(10)) # It will print the whole dataframe. It is similar to df.head() method.

json_path = "C:/PythonCode/Pandas/students_dummy.json"
df_json = pd.read_json(json_path, orient="records")
print("JSON DataFrame:")
print(df_json)

#JSON Structures:
#[{...}, {...}] — records ki list                             pd.read_json(path, orient="records")
#{...} — sirf ek record                                       json.load() + pd.DataFrame([data])
#{"20001": {...}, "20002": {...}} — key ke andar records      pd.read_json(path, orient="index")
#Har line par ek JSON object                                  pd.read_json(path, lines=True)
