#linearsearch
arr=[10,11,12,13,14,15,16]
element=int(input("Enter the element you want to search"))
flag=0
cnt=0
for num in arr:
    cnt+=1
    if(element==num):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("Element found")
else:
    print("Element not found")
print(cnt)