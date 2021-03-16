list1=[1,4,3]
list2=[3,4,5]
# t=[]
# for i in list1:
#     for j in list2:
#         t.append((i,j))
# print(t)

#by applying list comprehension

op=[(i,j)for i in list1 for j in list2]
print("printing the value pair",op)

square=[(i**2)for i in list1]
print(square)

p=[i for i in list1 if i%2==0]
print(p)

common=[i for i in list1 for j in list2 if(i==j)]
print(common)
