import os
import csv
from pathlib import Path
import logging
from PosgreSQLdb_connection import db_cursor

file_path = Path(__file__).parent / "employee_feed.csv" #path(__file__).parent gives the directory of the current script, and / "employee_feed.csv" appends the filename to that directory path, creating a complete path to the CSV file.
log_path = Path(__file__).parent / "logs" / "load_csv.log" #path(__file__).parent gives the directory of the current script, and / "load_csv.log" appends the filename to that directory path, creating a complete path to the log file.
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s') # Configure the logging module to write log messages to a file specified by log_path. The log level is set to INFO, meaning that messages with a severity level of INFO and above will be logged. The filemode='a' argument specifies that log messages should be appended to the file if it already exists. The format argument defines the structure of the log messages, including the timestamp, log level, and message content.
#logging.info("This is an info message")
#logging.warning("This is a warning message")
#logging.error("This is an error message")

def select_count(cur, row):
    cur.execute("SELECT COUNT(*) FROM stg_employee_feed WHERE employee_code = %s", (row['employee_code'],))    
    fetched_count = cur.fetchone()[0]  # fetchone() retrieves the first row of the result set, and [0] accesses the first column (the count value).
    print(f"Count of records in stg_employee_feed: {fetched_count}")
    logging.info(f"Count of records in stg_employee_feed: {fetched_count}")
    if fetched_count == 0:
        cur.execute("INSERT INTO stg_employee_feed (employee_code, employee_name, department, salary, city, joining_date) VALUES (%s, %s, %s, %s, %s, %s)",
                    (row['employee_code'], row['employee_name'], row['department'], row['salary'].strip() or None, row['city'], row['joining_date'])
                                        )
            
with open(file_path, "r", newline='', encoding='utf-8') as file:
    #reader = csv.reader(file)
    reader = csv.DictReader(file)  # DictReader reads the CSV file and returns each row as a dictionary, where the keys are the column headers and the values are the corresponding data for that row.
    with db_cursor() as cur:
        for row in reader:
            select_count(cur, row)  # Pass the cursor and the current row to the select_count function for processing.
            print(row)  # row is a standard list: ['Alice', 'Engineer', 'IT']

    
            


    