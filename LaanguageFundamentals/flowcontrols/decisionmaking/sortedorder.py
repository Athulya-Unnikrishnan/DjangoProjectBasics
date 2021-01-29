num1=int(input("Enter 1st number"))
num2=int(input("enter the 2nd number"))
num3=int(input("Enter 3rd number"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("num2 is secomd largest")
        print(num1,num2,num3)
    else:
        print("num3 is second largest")
        print(num1,num3,num2)
elif(num2>num3)&(num2>num1):
    if(num3>num1):
        print("num3 is 2nd largest")
        print(num2,num3,num1)
    else:
        print("num1 is second largest")
        print(num2,num1,num3)
else:
    if(num2>num1):
        print("num2 is 2nd largest")
        print(num3,num2,num1)
    else:
        print("num1 is 2nd largest")
        print(num3,num1,num2)