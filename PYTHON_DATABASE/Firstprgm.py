import mysql.connector

#connection database to python
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
)
cursor=mydb.cursor()
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)

print(mydb)
