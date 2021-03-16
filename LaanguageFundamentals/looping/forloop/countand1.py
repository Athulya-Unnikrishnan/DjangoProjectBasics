num=int(input("Enter a single digit number"))
sum=0
for i in range(1,num+1):
    pattern=str(num)*i
    sum = sum + int(pattern)
    # print(pattern)
print("sum is",sum)
