class Employee:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_details(self):
        print(self.name," ",self.age)

emp=Employee("Athulya",24) #constructor is called and instance variables is initialized inside __init__() method
emp.print_details()