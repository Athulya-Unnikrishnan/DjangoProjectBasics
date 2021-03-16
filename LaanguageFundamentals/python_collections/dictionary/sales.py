expenses={"jan":2800,"feb":30000,"March":40000,"April":38000,"May":35000}

print(expenses["April"])
for k in expenses:
    print(k)

for k,v in expenses.items():
    print(k,v)

#updation
expenses["April"]-=2000