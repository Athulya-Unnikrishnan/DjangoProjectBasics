students=[
    {"name":"Varun","desig":"Devop","Salary":40000,"join":2000,"resign":2008},
    {"name":"Ram","desig":"Devop","Salary":30000,"join":1989,"resign":1995},
    {"name":"Raju","desig":"QA","Salary":28000,"join":2004,"resign":2010},
    {"name":"Ravi","desig":"QA","Salary":32000,"join":2005,"resign":2015},
    {"name":"Sravan","desig":"Marketing","Salary":35000,"join":2010,"resign":2020}
]

#highest salary

high=(max(list(map(lambda dict:dict["Salary"],students))))
print(high)

#employees having experience greater than 8

exp=list(filter(lambda emp:emp["resign"]-emp["join"]>8,students))
print(exp)