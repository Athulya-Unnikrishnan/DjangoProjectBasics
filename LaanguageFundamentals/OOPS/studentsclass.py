class Student:
    def set_details(self,roll,name,total):
        self.roll=roll
        self.name=name
        self.total=total
    def get_details(self):
        print("Roll No:",self.roll)
        print("Name :",self.name)
        print("TotaL Mark ",self.total)

stud=Student()
stud.set_details(101,"Athulya",100)
stud.get_details()