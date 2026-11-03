from db_connection import connect_to_postgresql

#connection = None removed from here .
def add_employee():
    connection = None # Initialize the connection variable to None. Initializing it to None allows us to check later if the connection was successful before attempting to close it in the finally block.
    v_department = input("Enter the department name: ") # Prompt the user to enter a department name. The input() function captures user input from the console and stores it in the v_department variable.
    v_employee_name = input("Enter the employee name: ") # Prompt the user to enter an employee name. The input() function captures user input from the console and stores it in the v_employee_name variable.
    v_salary = float(input("Enter the salary: ")) # Prompt the user to enter a salary. The input() function captures user input from the console, and float() converts it to a floating-point number.
    v_city = input("Enter the city: ") # Prompt the user to enter a city. The input() function captures user input from the console and stores it in the v_city variable.
    v_joining_date = input("Enter the joining date (YYYY-MM-DD): ") # Prompt the user to enter a joining date. The input() function captures user input from the console and stores it in the v_joining_date variable.
    
    try:
        connection = connect_to_postgresql()

        with connection.cursor() as cursor:
            insert_query = """
                INSERT INTO employees (employee_name,department,salary,city,joining_date)
                VALUES (%s, %s, %s, %s, %s)
            """ # Define an SQL INSERT query with placeholders for parameterized values. This helps prevent SQL injection attacks.

            cursor.execute(insert_query, (v_employee_name, v_department, v_salary, v_city, v_joining_date)) # Execute the INSERT query with the provided values.

            connection.commit() # Commit the transaction to save changes to the database.

            print("Employee added successfully.")

    except Exception as error:
        print("Failed to add employee:", error)

    finally:
        if connection is not None:
            connection.close()
            print("Connection closed.")
#add_employee() # Call the add_employee function to execute the process of adding a new employee to the database.

def update_employee():
    connection = None
    v_employee_name = input("Enter the employee name to update: ") # Prompt the user to enter the employee name to update.
    v_new_salary = float(input("Enter the new salary: ")) # Prompt the user to enter a new salary. The input() function captures user input from the console, and float() converts it to a floating-point number.

    try:
        connection = connect_to_postgresql()

        with connection.cursor() as cursor:
            update_query = """
                UPDATE employees
                SET salary = %s
                WHERE employee_name = %s
            """ # Define an SQL UPDATE query with placeholders for parameterized values.

            cursor.execute(update_query, (v_new_salary, v_employee_name)) # Execute the UPDATE query with the provided values.
            if cursor.rowcount != 0:
                connection.commit() # Commit the transaction to save changes to the database.

                #print("Employee salary updated successfully."+str(cursor.rowcount))
                print(f"Employee salary updated successfully. Rows updated: {cursor.rowcount}") # More readable output using f-string formatting to display the number of rows updated.
            else:
                print("Employee not found.")

    except Exception as error:
        print("Failed to update employee:", error)

    finally:
        if connection is not None:
            connection.close()
            print("Connection closed.")

def delete_employee():
    connection = None
    v_employee_name = input("Enter the employee name to delete: ") # Prompt the user to enter the employee name to delete.

    try:
        connection = connect_to_postgresql()

        with connection.cursor() as cursor:
            delete_query = """
                DELETE FROM employees
                WHERE employee_name = %s
            """ # Define an SQL DELETE query with a placeholder for the employee name.

            cursor.execute(delete_query, (v_employee_name,)) # Execute the DELETE query with the provided employee name.
            if cursor.rowcount != 0:
                connection.commit() # Commit the transaction to save changes to the database.

                print(f"Employee deleted successfully. Rows deleted: {cursor.rowcount}") # More readable output using f-string formatting to display the number of rows deleted.
            else:
                print("Employee not found.")

    except Exception as error:
        print("Failed to delete employee:", error)

    finally:
        if connection is not None:
            connection.close()
            print("Connection closed.")