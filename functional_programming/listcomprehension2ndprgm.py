#take the values from list and check if the number is greater than 5 and if its true subtract with 1 and
#else add with 1 to a new list "lis"
list1=[3,4,2,6,7,8]
lis=[i-1 if(i<5) else i+1 for i in list1]
print(lis)