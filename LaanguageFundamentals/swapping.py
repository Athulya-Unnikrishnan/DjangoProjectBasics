num1=10
num2=20
num3=num1
num1=num2
num2=num3
print("num1= ",num1,"num2 =",num2)

#othermethod without using 3rd variable
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1,num2)

#othermethod only used in python
num1,num2=num2,num1
print(num1,num2)