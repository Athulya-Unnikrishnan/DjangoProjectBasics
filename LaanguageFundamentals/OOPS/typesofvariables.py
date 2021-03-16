class Employee:
    company_name="ctc"
    def set_person(self,age,name):
        self.age=age
        self.name=name
    def print_person(self):
        print(self.age)
        print(self.name)
        print(Employee.company_name)

emp=Employee()
emp1=Employee()
emp1.set_person(23,"ramu")
emp1.print_person()
emp.set_person(25,"ram")
print(emp.age)
print(Employee.company_name)