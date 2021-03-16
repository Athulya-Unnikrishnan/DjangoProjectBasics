f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    #print(lines)
    #break
    data=lines.rstrip("\n").split(",")
    #print(data)
    state=data[3]
    confirmed_cases=int(data[-1])
    dict[state]=confirmed_cases

for k,v in dict.items():
    print(k,"==>",v)
#print("Highest confirmed cases is in ",max(dict,key=dict.get))
result=max(dict,key=dict.get)
print(result,dict[result])
