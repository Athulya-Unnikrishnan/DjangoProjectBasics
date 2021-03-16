lst=[1,2,3,4,5,6,7,8,9]

#even numbers
even=list(filter(lambda num:num%2==0,lst))
print(even)

#number greater than 3
number=list(filter(lambda num:num>3,lst))
print(number)