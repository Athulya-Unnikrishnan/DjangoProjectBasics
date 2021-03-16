num=int(input("Enter a number"))
flag=0
for i in range(20,51):
    if(num==i):
        flag=1
        break
    else:
        flag=0
if(flag==0):
    print("It doesn't includes in the range")
else:
    print("It includes in the range")

#2nd method without for loop
# if num in range(20,51):
#     print("true")
# else:
#     print("false")