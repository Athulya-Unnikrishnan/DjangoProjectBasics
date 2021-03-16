class Person:
    def set_person(self,age,name):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name)
        print(self.age)

obj=Person()
obj.set_person(25,"Athulya")
obj.print_person()

obj2=Person()
obj2.set_person(26,"Athulya Unnikrishnan")
obj2.print_person()