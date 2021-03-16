# __init__() method is inside object class and object class is inherited by Person(automatically) thats y
# __init__ method is executed because its inside the object class(builtin)
#
class Person():
    def __init__(self,age,name):
        self.age=age
        self.name=name

    # def __str__(self):
    #     return self.name+" "+str(self.age)

p=Person(25,"ATHULYA")
P1=Person(24,"Unni")
#whenever we tries to print the object of the class it automatically callls the builtin method def__str__(): inside
# the object class and returns the reference of that object
# if we need to print the name of the person by printing the objecr we have to override the __str__ method inside the
# Person class which we have created that is it will return the name and age of the Person
print(p)
print(P1)
#if we try to print the object of the class it will show the reference of the object
#<__main__.Person object at 0x0000024033D1B8E0>
#<__main__.Person object at 0x00000240335EA250>
