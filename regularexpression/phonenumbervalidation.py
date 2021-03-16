from re import *


rule='([+])?(91)?[0-9]{10}' #"?" is used for optional

variablename=input("Enter a variablename")

match=fullmatch(rule,variablename)
if match!=None:
    print("valid")
else:
    print("invalid")