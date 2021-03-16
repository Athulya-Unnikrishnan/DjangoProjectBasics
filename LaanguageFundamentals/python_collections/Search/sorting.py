arr=[12,15,11,10,19,16]
for i in range(0,len(arr)):
    for j in range(len(arr)):
        if(arr[i]<=arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
