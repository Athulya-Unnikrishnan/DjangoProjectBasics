employee={"Id":101,"Name":"Athulya","Designation":"Python Developer","Salary":35000}
print("Name of the employee :",employee["Name"])
print("Salary :",employee["Salary"])
if "Gender" in employee:
    print("Gender key is present")
else:
    employee["Gender"]="Female"
print(employee)

for k,v in employee.items():
    print(k,":",v)