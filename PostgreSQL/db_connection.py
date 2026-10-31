import psycopg2
import os # os module is used to access environment variables and interact with the operating system.
from dotenv import load_dotenv

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