# #we can use sort() function to sort list values
# #arr.sort() here sort is a method that is, sort function is inside a class
# #data=sorted(arr) here sorted is a function
# arr=[10,11,12,13,14,15,16]
# element=int(input("Enter the element to be searched"))
# lower=0
# upper=len(arr)-1
# flag=0
# cnt=0
# while(lower<=upper):
#     cnt+=1
#     mid=upper+lower//2
#     if(element>arr[mid]):
#         lower=mid+1
#     elif(element<arr[mid]):
#         upper=mid-1
#     elif(element==arr[mid]):
#         flag=1
#         break
# if(flag==1):
#     print("Element found")
# else:
#     print("Element not found")
# print(cnt)

lst1=[10,20,21,22]
lst2=[11,12,10,20]


elements=set(lst1).intersection(set(lst2))
print(elements)