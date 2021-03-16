f=open('words',"r")
#lst=[]
dict={}
for lines in f:
    #print(lines)
    words=lines.rstrip("\n").split(" ")
    #lst.append(words)
#print(lst)
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
#print(dict)
for k,v in dict.items():
    print(k,"==>",v)

#SORT
data=sorted(dict,key=dict.get,reverse=True)
print(data)
