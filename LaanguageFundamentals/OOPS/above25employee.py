lst=[]
class Person:
    def __init__(self,age,name):
         self.age=age
         self.name=name

p=Person(27,"Ram")
p1=Person(26,"Varun")
p2=Person(25,"Nikil")
lst.append(p)
lst.append(p1)
lst.append(p2)
#persons whose age is greater than 25
for psn in lst:
    if psn.age>25:
        print(psn.name)

#print highest age
agelist=[]
for psn in lst:
    agelist.append(psn.age)
print(max(agelist))

#or use a variable check
check=0
for psn in lst:
    if(psn.age>check):
        check=psn.age
print(check)