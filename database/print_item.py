import mysql.connector

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="python_database"
    )
    cursor=mydb.cursor()
    query="SELECT * from table_name"
    cursor.execute(query)
    data=cursor.fetchall()
    for item in data:
        print(item)
    mydb.commit()

except Exception as e:
    print(e)
    
