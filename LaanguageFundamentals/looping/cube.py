i=int(input("Enter a 3 didgit number"))
sum=0
while(i!=0):
    dig=i%10
    print(dig,end="^3+")
    c=dig**3
    sum=sum+c
    i=i//10
print("\n")
print("sum is",sum)