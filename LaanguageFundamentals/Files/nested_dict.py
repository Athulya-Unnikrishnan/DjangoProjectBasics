f=open("covid_19_india.csv","r")
dict={}
#dicty={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmed_cases=int(data[-1])
    cured_cases=int(data[-2])
    death_cases=int(data[-3])
    dict[state]={"state":state,"confirmed_cases":confirmed_cases,"cured cases":cured_cases,"death cases":death_cases}
#print(dict)
   # print("State: ",dict[state]["state"],"==>","Confimed Cases",dict[state]["confirmed_cases"])
for k,v in dict.items():
    print("State: ", dict[k]["state"], "==>", "Confimed Cases", dict[k]["confirmed_cases"])
#print(k,"==>",v)