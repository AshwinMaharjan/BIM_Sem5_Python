import mysql.connector

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="python_database"
    )
    cursor=mydb.cursor()
    query="INSERT into `table_item`(`item_name`,`rate`,`stock`,`photo`,`remarks`) VALUES(%s,%s,%s,%s,%s)"
    item=('from python',200,0,'','good')
    cursor.execute(query,item)
    mydb.commit()
    print("Success")
except Exception as e:
    print(e)