from re import *

f=open("vehicleregistration number","r")
rule='KL\d{2}[A-Z]{2}\d{1,4}'
lst=[]
for lines in f:
    variable=lines.rstrip("\n")
    match=fullmatch(rule,variable)
    if match!=None:
        lst.append(variable)
print(lst)



#Google
# ^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$
# ^ means start of string
# [A-Z]{2} means 2 characters in the range of A through Z
# \s means white space
# [0-9]{2} means 2 characters in the range of 0 through 9
# \s means white space
# [A-Z]{2} means 2 characters in the range of A through Z
# \s means white space
# [0-9]{4} means 4 characters in the range of 0 through 9
# $ means end of string






