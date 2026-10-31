import psycopg2
from db_connection import connect_to_postgresql # Import the connect_to_postgresql function from the db_connection module. This function is responsible for establishing a connection to the PostgreSQL database using the provided credentials.

connection = None

try:
    # Get database connection
    connection = connect_to_postgresql()

    # Create cursor
    with connection.cursor() as cursor:

        # Execute SQL query
        cursor.execute(
            "SELECT current_database(), current_user;"
        )

        # Fetch result
        result = cursor.fetchone()

        print("Database:", result[0])
        print("User:", result[1])

except psycopg2.Error as error:
    print("SQL execution failed:", error)

finally:
    if connection is not None:
        connection.close()
        print("Connection closed.")