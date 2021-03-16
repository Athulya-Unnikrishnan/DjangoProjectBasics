#read data from file and insert into table (mysql)
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="company"
)
cursor=mydb.cursor()

f=open("data","r")
for lines in f:
    values=lines.rstrip("\n")
    datas=values.split(",")
    sql="insert into employee values(%s,%s)"
    record=(datas[0],datas[1])
    cursor.execute(sql,record)
    mydb.commit()

print("value inserted")