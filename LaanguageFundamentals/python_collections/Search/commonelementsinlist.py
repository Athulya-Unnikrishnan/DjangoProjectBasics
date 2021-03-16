lis1=[10,13,11,14,18]
lis2=[10,13,12,15]
lis1.sort()
lis2.sort()
for i in lis1:
    for j in lis2:
        if(i==j):
            print(i," ",end="")

#2nd method which reduces time complexity of the above program to O(n)

arr1=[10,13,11,14,18]
arr2=[10,13,12,15]
pos1=0
pos2=0
while(pos1<len(arr1)&pos2<len(arr2)):
    if(arr1[pos1]==arr2[pos2]):
        print(arr1[pos1])
        pos1+=1
        pos2+=1
    elif(arr1[pos1]>arr2[pos2]):
        pos2+=1
    else:
        pos1+=1



