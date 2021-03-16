#single inheritance
class Parent:

    def phone(self):
        print("Phone method is inside Parent class")

class child(Parent):
    pass

ch=child()
ch.phone()

#multi level inheritance
class Parent:
    def read(self):
        print("Read merthod inside parent class")
class Subchild(Parent):
    def write(self):
        print("Write method inside Subchild class")
class child(Subchild):
    def print_functions(self):
        print("Print method inside child class")

ch=child()
ch.read()
ch.write()
ch.print_functions()


#multiple inheritance
class Parent:
    # def read(self):
    #     print("Read merthod inside parent class")
    def write(self):
        print("Read merthod inside parent class")
class Subchild():
    def write(self):
        print("Write method inside Subchild class")
class child(Subchild,Parent):
    def print_functions(self):
        print("Print method inside child class")

ch=child()
#ch.read()
ch.write()
ch.print_functions()
