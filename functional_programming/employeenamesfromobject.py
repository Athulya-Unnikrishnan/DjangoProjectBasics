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


# for emp in employees:#here emp is an object
#     print(emp)
#instead of using the above for loop we can use the lambda and map function to read the employee names from an object

# ename=list(map(lambda emp:emp.name,employees))#emp is an object in this case
# print(ename)
#to print names of the employees whose designation is developer
des=list(map(lambda emp:emp.name,list(filter(lambda emp:emp.desig=="Developer",employees))))
print(des)

#print details of the employees whose experience is greater than 2
experience=list(filter(lambda emp:int(emp.exp)>2,employees))
print(experience)

count=len(list(filter(lambda emp:emp.desig=="QA",employees)))
print(count)


#maximum salary
#using reduce
# from functools import reduce
# high=list(reduce(lambda emp1,emp2:emp1.salary if(emp1.salary>emp2.salary) else emp2.salary,employees))
# print(high)
#error is occured because it is taking arguments as integer values (emp1,emp2) and it is taking salary
#from  "emp1.salary" that is int.salary and in our program salary is taken from object.salary
#and we cannt take salary from object.salary because reduce takes integer values only
#so to find maximum salary we use max function and map function

highest=max(list(map(lambda emp:emp.salary,employees)))
print(highest)