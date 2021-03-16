import mysql.connector

#insert into table
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="company"
)
cursor=mydb.cursor()
sql="select * from employee"
cursor.execute(sql)
data=cursor.fetchall()
print(data)




