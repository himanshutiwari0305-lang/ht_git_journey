
import psycopg2 #psycopg2 is a PostgreSQL adapter for Python that allows you to connect to a PostgreSQL database and execute SQL queries.
from contextlib import contextmanager
import os
from dotenv import load_dotenv #initially i got error "ModuleNotFoundError: No module named 'dotenv'" so i installed it using pip install python-dotenv

load_dotenv()# Load environment variables from a .env file into the program's environment. This allows you to keep sensitive information, such as database credentials, separate from your codebase.

def connect_to_postgresql(): # Whenever Python code needs to connect to the PostgreSQL database, it can call this function. This promotes code reusability and makes it easier to manage database connections in a centralized manner.
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        ) # Establish a connection to the PostgreSQL database using the provided credentials. The connection parameters are retrieved from environment variables.

        print("PostgreSQL connection successful!")

        return connection # Return the connection object to the caller so that it can be used for executing queries and interacting with the database.

    except psycopg2.Error as error:
        print("Database connection failed:", error)
        raise

@contextmanager
def db_cursor(commit=True): 
    conn = connect_to_postgresql()          # must raise on failure
    try:
        with conn.cursor() as cur:
            yield cur   # yeild cur allows the caller to use the cursor object within a with statement, ensuring that the cursor is properly closed after use.
        if commit:
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
#try:
#    connection = psycopg2.connect(
#        host=os.getenv("DB_HOST"),
#        port=os.getenv("DB_PORT"),
#        database=os.getenv("DB_NAME"),
#        user=os.getenv("DB_USER"),
#        password=os.getenv("DB_PASSWORD")
#    ) # Establish a connection to the PostgreSQL database using the provided credentials. The connection parameters are retrieved from environment variables.

#    print("PostgreSQL connection successful!")

#    cursor = connection.cursor()
#    cursor.execute(
#        "SELECT current_database(), current_user;"
#    ) # connection.cursor() creates a cursor object that allows you to execute SQL queries and fetch results. The execute() method is used to run the SQL query "SELECT current_database(), current_user;" which retrieves the name of the current database and the current user.

#    result = cursor.fetchone() # cursor.fetchone() retrieves the first row of the result set returned by the executed query. In this case, it will contain the current database name and the current user.
#    print("Database:", result[0])
#    print("User:", result[1])

#except psycopg2.Error as error:
#    print("Database connection failed:", error)

#finally:
#    if "connection" in locals() and connection is not None: # connection is not None checks if the connection object exists and is not None before attempting to close it. This prevents errors in case the connection was never established.
#        connection.close() # Once connction.close() is called, the connection to the database is terminated, and any resources associated with it are released. Then connection will become None, and you won't be able to use it to execute queries or interact with the database anymore.
#        print("Connection closed.")
