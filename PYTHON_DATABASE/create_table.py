import mysql.connector

#create table
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="company"
)
cursor=mydb.cursor()
sql="create table employee(id int,name varchar(50))"
cursor.execute(sql)

print("Table created")


