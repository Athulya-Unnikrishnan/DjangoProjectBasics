from re import *

pattern="ab"
source="abababaaaaab"

matcher=finditer(pattern,source)
count=0
for match in matcher:
    print("Pattern starting position",match.start())
    print(match.group())
    count+=1
print("Number of times pattern is matched is: ",count)