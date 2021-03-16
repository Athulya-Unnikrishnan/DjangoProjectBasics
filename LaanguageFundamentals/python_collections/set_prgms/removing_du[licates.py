lst=[1,2,3,4,5]
num=int(input("Enter a number"))
st=set(lst)
out=set()#to remove duplicates
for s in st:
    op=num-s
    if op in lst:
        if(s>op):
            out.add((op,s))
        elif(s==op):
            pass
        else:
            out.add((s,op))
print(out)