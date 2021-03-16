import mysql.connector

#insert into table
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="company"
)
cursor=mydb.cursor()
sql="insert into employee values(1,'Athulya')"
cursor.execute(sql)
mydb.commit()

print("value inserted")


