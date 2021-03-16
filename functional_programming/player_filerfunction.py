#to print players name whose matches are greater than 320

players=[
    {"name":"Sachin","matches":500,"rank":1},
    {"name": "Dravid", "matches": 450, "rank": 12},
    {"name": "Sachin", "matches": 300,"rank":23},
    {"name": "Sac", "matches": 400,"rank":23}
]


match=list(filter(lambda dict:dict["matches"]>320,players))
print(match)#filter will return the whole object that satisfies the condition

#if we want to print only the names of the player whose matches is greater than 320
match=list(map(lambda player:player["name"],list(filter(lambda dict:dict["matches"]>320,players))))
print(match)

