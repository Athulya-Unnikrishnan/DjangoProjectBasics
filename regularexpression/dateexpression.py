from re import *
rule="0[0-9]-|[1][0-9]-|2[0-9]-|3[01]-"
variablename=input("Enter a variablename")

match=fullmatch(rule,variablename)
if match!=None:
    print("valid")
else:
    print("invalid")