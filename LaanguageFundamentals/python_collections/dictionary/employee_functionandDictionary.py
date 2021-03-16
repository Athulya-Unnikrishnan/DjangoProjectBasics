employee={1001:{"emp_id":1001,"emp_name":"Athu","Designation":"Python Developer","Salary":30000},
    1002:{"emp_id":1002,"emp_name":"Athul","Designation":"Python Developer","Salary":40000},
    1003:{"emp_id":1003,"emp_name":"Athulya","Designation":"Python Developer","Salary":50000}

}
def details(**kwargs):
    #print(kwargs)
    id=kwargs["emp_id"]
    print(id)
    if id in employee:
        if "Prop" in kwargs:
            print(employee[id]["emp_name"])
            Property = kwargs["Prop"]
            if(Property=="Designation"):
                print(employee[id]["Designation"])
            elif(Property=="Salary"):
                print(employee[id]["Salary"])
        else:
            print(employee[id]["emp_name"])
            print(employee[id]["Designation"])
            print(employee[id]["Salary"])

details(emp_id=1001)
