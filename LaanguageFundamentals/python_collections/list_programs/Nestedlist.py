employees=[[100,"Athu","Pythondeveloper",25000],
           [200,"Athulya","Python",35000],
           [300,"Athulya U","developer",45000],
           [400,"Athulya Unnikrishan","Pythondeveloper",55000]]
sum=0
sal=0
for emp in employees:
    #print(emp)
    print(emp[1])

for emp1 in employees:
    if(emp1[2]=="Pythondeveloper"):
        print(emp1)

for emp2 in employees:
    #print(emp[3])
    sum=sum+emp[3]
print("salary sum "sum)

for emp2 in  employees:
   if(emp2[3]>sal):
       sal=emp2[3]
print("highest salary is ",emp2[3])

#2nd method for finding highest salary
sallist=[]
for e in employees:
    sallist.append(e[3])
print("highest salary is ",max(sallist))