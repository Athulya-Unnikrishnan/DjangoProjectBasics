from new_math_module import *
n=add(2,3)
s=difference(2,3)
p=product(2,4)
print(n)
print(s)
print(p)




#####without from
print("2nd method")
import new_math_module
n=new_math_module.add(2,3)
s=new_math_module.difference(2,3)
p=new_math_module.product(2,4)
print(n)
print(s)
print(p)


###if the module file is present in another directory and we are doing the program in different directory do this
# print("module and currently working file are present in different directory")
# print("current working directory name is testwork and file name is calc.py")
# import function.new_math_module
# n=function.new_math_module.add(2,3)
# s=function.new_math_module.difference(2,3)
# p=function.new_math_module.product(2,4)
# print(n)
# print(s)
# print(p)
#
