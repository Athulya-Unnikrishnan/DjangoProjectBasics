class Maths:
    def add(self):
        print("inside no arg")
    def add(self,num1):
        print("inside 1 args")
    def add(self,num1,num2):
        print("inside 2 args")

math=Maths()
math.add(10,10)

#in python only the recently created method will be invoked




