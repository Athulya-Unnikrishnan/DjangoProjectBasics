from re import *


rule='[a-zA-Z]+[0-9]*@gmail.com'

variablename=input("Enter a variablename")

match=fullmatch(rule,variablename)
if match!=None:
    print("valid")
else:
    print("invalid")