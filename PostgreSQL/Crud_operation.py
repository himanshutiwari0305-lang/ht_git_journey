from db_connection import connect_to_postgresql

connection = None # Initialize the connection variable to None. Initializing it to None allows us to check later if the connection was successful before attempting to close it in the finally block.
def add_employee():
    v_department = input("Enter the department name: ") # Prompt the user to enter a department name. The input() function captures user input from the console and stores it in the v_department variable.
    v_employee_name = input("Enter the employee name: ") # Prompt the user to enter an employee name. The input() function captures user input from the console and stores it in the v_employee_name variable.
    v_salary = float(input("Enter the salary: ")) # Prompt the user to enter a salary. The input() function captures user input from the console, and float() converts it to a floating-point number.
    v_city = input("Enter the city: ") # Prompt the user to enter a city. The input() function captures user input from the console and stores it in the v_city variable.
    v_joining_date = input("Enter the joining date (YYYY-MM-DD): ") # Prompt the user to enter a joining date. The input() function captures user input from the console and stores it in the v_joining_date variable.
    print("control reached")
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