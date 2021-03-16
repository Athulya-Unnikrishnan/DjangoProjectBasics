arr=[13,12,13,14,15,13,16]
arr.sort()
print("sorted array is ",arr)
num=int(input("enter the element"))
upper=len(arr)-1
print("upper value is ",upper)
for i in range(1,upper):
    print("i value is ",i)
    if(arr[upper]!=num):
        print("ELEMENT IN THE UPPERVALUE IS ", arr[upper])
        temp=arr[upper]
        arr[upper]=arr[upper-1]
        arr[upper-1]=temp
        print("swapped elements are ",arr[upper],arr[upper-i])
        print(arr)
