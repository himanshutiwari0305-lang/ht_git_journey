import os
import csv
from PosgreSQLdb_connection import db_cursor

print(os.getcwd())
def select_count():
    with db_cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM stg_employee_feed WHERE employee_code = %s", (row['employee_code'],))    
        fetched_count = cur.fetchone()[0]  # fetchone() retrieves the first row of the result set, and [0] accesses the first column (the count value).
        print(f"Count of records in stg_employee_feed: {fetched_count}")
        if fetched_count == 0:
            cur.execute("INSERT INTO stg_employee_feed (employee_code, employee_name, department, salary, city, joining_date) VALUES (%s, %s, %s, %s, %s, %s)",
                            (row['employee_code'], row['employee_name'], row['department'], row['salary'].strip() or None, row['city'], row['joining_date'])
                                        )
            
with open("PostgreSQL/employee_feed.csv", "r") as file:
    #reader = csv.reader(file)
    reader = csv.DictReader(file)  # DictReader reads the CSV file and returns each row as a dictionary, where the keys are the column headers and the values are the corresponding data for that row.
    for row in reader:
        select_count()
        print(row)  # row is a standard list: ['Alice', 'Engineer', 'IT']

    
            


    