i=int(input("Enter a 3 didgit number"))
while(i!=0):
    dig=i%10
    print(dig,end="")#or string approcah res="",res=res+str(dig) or integer approach res=0 res=res*10+dig
    i=i//10




