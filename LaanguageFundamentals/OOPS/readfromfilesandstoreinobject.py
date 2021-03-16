# read each lines from file "employeedetails" den store each lines in each object

class Employee:

    def __init__(self,eid,name,desig,salary,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.salary=salary
        self.exp=exp
    def __str__(self):
        return self.name

f=open("employeedetails","r")
employees=[]
for lines in f:
    eid,name,desig,salary,exp=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,name,desig,salary,exp))
    #employees list will store objects
for emp in employees:#here emp is an object
    print(emp)
#to print highest salary
sal=[]
for emp in employees:
    sal.append(emp.salary)
print(max(sal))