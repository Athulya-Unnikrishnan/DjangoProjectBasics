from re import *
#
# pattern="[ab]" #either a or b
# source="abababaaaaab"
#
# matcher=finditer(pattern,source)
# count=0
# for match in matcher:
#     print("Pattern starting position",match.start())
#     print(match.group())
#     count+=1
# print("Number of times pattern is matched is: ",count)



#if pattern="[a-z]" means checking lowecase letters from a to z


#
pattern='\W'
source="ab 9eD"

matcher=finditer(pattern,source)
count=0
for match in matcher:
    print("Pattern starting position",match.start())
    print(match.group())
