from re import *


rule='KL\d{2}[A-Z]{2}\d{1,4}'

variablename=input("Enter a variablename")

match=fullmatch(rule,variablename)
if match!=None:
    print("valid")
else:
    print("invalid")