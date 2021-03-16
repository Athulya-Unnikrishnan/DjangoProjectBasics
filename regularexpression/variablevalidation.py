from re import *


rule='[a-kA-K][369][a-zA-Z0-9]*'

variablename=input("Enter a variablename")

match=fullmatch(rule,variablename)
if match!=None:
    print("valid")
else:
    print("invalid")