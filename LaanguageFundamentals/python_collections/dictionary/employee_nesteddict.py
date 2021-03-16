employee={1001:{"emp_id":1001,"emp_name":"Athu","Designation":"Python Developer","Salary":30000},
    1002:{"emp_id":1002,"emp_name":"Athul","Designation":"Python Developer","Salary":40000},
    1003:{"emp_id":1003,"emp_name":"Athulya","Designation":"Python Developer","Salary":50000}

}

id=int(input("Enter the employee id"))
Property=input("Enter the property").lower()
if id in employee:
    print("Name of the employee :",employee[id]["emp_name"])
    if Property in employee[id]:
        print(Property,": ",employee[id][Property])
    else:
        print("Invalid Property")
else:
    print("Invalid id")
