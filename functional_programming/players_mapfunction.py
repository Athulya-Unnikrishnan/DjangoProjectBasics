#to print players name

players=[
    {"name":"Sachin","matches":500,"rank":1},
    {"name": "Dravid", "matches": 450, "rank": 12},
    {"name": "Sachin", "matches": "300","rank":23}

]


nam=list(map(lambda dict:dict["name"],players))
print(nam)

rank=list(map(lambda dict:dict["rank"],players))
print(rank)