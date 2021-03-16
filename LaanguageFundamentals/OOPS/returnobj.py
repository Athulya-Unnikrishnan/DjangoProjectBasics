class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        #self takes obj and others will take obj1
        #self.pages means obj.pages and others.pages means obj1.pages
        #return self.pages+other.pages
    #now if we want to add 3 objects we have to convert the first 2 values into Book because
    # obj and obj1 is converted into integer after addition
       return Book(self.pages+other.pages)
    def __sub__(self,other):
        return self.pages-other.pages
    def __str__(self):
        print("inside")
        return str(self.pages)

obj=Book(100)
obj1=Book(200)
obj2=Book(100)
print(obj+obj1+obj2)
#print(obj+obj1)