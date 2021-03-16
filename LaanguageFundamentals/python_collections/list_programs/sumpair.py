# value=[4,2,3,7]
# sum=int(input("Enter the sum value whose pair values includes in the list"))
# for i in value:
#     for j in value:
#         if(i+j==sum)&(i!=j)&(i<j):
#             print(i,j)


#2nd method having time complexity is O(n)

value=[4,2,3,7]
value.sort()
sum=int(input("Enter the sum value"))
lower=0
upper=len(value)-1
while(lower<upper):
    v=value[lower]+value[upper]
    if(v==sum):
        print(value[lower],value[upper])
        lower+=1
        upper-=0

    elif(v>sum):
        upper-=1
    elif(v<sum):
        lower+=1
