class swift:
    def start(self):
        print("Swift started")
    def accelarate(self):
        print("Swift accelerated")
    def stop(self):
        print("Stop swift")

class bmw:
    def start(self):
        print("bmw started")
    def accelarate(self):
        print("bmw accelerated")
    def stop(self):
        print("Stop bmw")

class Person:
    def drive(self,car):
        car.start()
        car.accelarate()
        car.stop()

sw=swift()#object of swift
p=Person()#object of the person class
p.drive(sw)#calling the methods inside the swift class using the object of swift class



####2nd program
class pycharm:
    def createfile(self):
        print("pycharm createfile")
    def executeprgm(self):
        print("pycharm execute")
class vscode:
    def createfile(self):
        print("vscode createfile")
    def executeprgm(self):
        print("vscode execute")

class Programmer:
    def coding(self,ide):
        ide.createfile()
        ide.executeprgm()

p=Programmer()
py=pycharm()
p.coding(py)