text="hello hai hello hai hello hai hai"
words=text.split(" ")
#print(words)
dict={}
count=0
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
print(max(dict,key=dict.get))

#sort
print(sorted(dict,key=dict.get,reverse=True))