import matplotlib.pyplot as plt

f=open("covid_19_india.csv","r")
dict={}
Confirmed_Cases=[]
States=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    State=data[3]
    confirmed=data[-1]
    dict[State]=confirmed
#print(dict)

for values in dict:
    Confirmed_Cases.append(dict[values])
    States.append(values)

plt.bar(States,Confirmed_Cases)
plt.title("Confirmed Cases in India State-wise Report")
plt.xlabel("States")
plt.ylabel("Confirmed Cases")
plt.show()
