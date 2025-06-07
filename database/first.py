import mysql.connector as conn

try:
    # Try connecting to the database
    connection = conn.connect(
        host="localhost",
        user="root",
        password="",  # Put your MySQL password here if there is one
        database="python_database"  # Make sure this database exists
    )
    print("MySQL database connected!")
    connection.close()

except conn.Error as e:
    print("Connection failed!")
    print("Error:", e)
