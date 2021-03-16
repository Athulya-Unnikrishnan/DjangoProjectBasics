num=int(input("Enter the exponential value"))
lower=int(input("Enter the lower limit"))
upper=int(input("Enter the upper imit"))
for i in range(1,upper):
    val=i*+num
    if val in range(lower,upper):
        print(val)