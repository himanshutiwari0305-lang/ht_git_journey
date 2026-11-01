from db_connection import connect_to_postgresql

connection = None # Initialize the connection variable to None. Initializing it to None allows us to check later if the connection was successful before attempting to close it in the finally block.    
v_department = input("Enter the department name: ") # Prompt the user to enter a department name. The input() function captures user input from the console and stores it in the v_department variable.
v_employee_name = input("Enter the employee name: ") # Prompt the user to enter an employee name. The input() function captures user input from the console and stores it in the v_employee_name variable.
try:
    connection = connect_to_postgresql()

    with connection.cursor() as cursor:

        #cursor.execute("SELECT * FROM employees") # In this case, it retrieves all rows from the "employees" table. The execute() method is used to run SQL queries against the database. 
        #cursor.execute("SELECT * FROM employees WHERE department = 'IT'") # Where clause usage.
        #cursor.execute("SELECT * FROM employees WHERE department = %s AND employee_name = %s", (v_department, v_employee_name)) # Where clause usage using parameterized queries. The %s placeholder is used to safely insert the value of v_department into the query, preventing SQL injection attacks. The second argument is a tuple containing the value to be substituted into the query.
        cursor.execute("SELECT salary,city,joining_date FROM employees WHERE department = %s AND employee_name = %s", (v_department, v_employee_name))

        results = cursor.fetchall() # fetchall() retrieves all rows of the result set returned by the executed query. In this case, it will contain all records from the "employees" table.
        if results:
            for row in results:
                print(row)
        else:
            print("No matching records found.")

except Exception as error:
    print("Query execution failed:", error)

finally:
    if connection is not None:
        connection.close()
        print("Connection closed.")