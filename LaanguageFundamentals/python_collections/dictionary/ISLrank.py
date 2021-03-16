ISL={"MumbaiCity":34,"Kerala Blasters":16,"Chennaian":17,"Bengaluru":19}
lst=[]
# for k in ISL:
#     lst.append(ISL[k])
# lst.sort()
# print(lst)
# i=len(lst)-1
# for
# print(lst[i])
# while(i>=0):
#     for k,v in ISL.items():
#         if(ISL[k]==lst[i]):
#             print(k,v)
#     i-=1

#
# for k,v in ISL.items():
#     lst.append(ISL[k])
#     lst.sort()
#     i=len(lst)-1
#     if(ISL[k]==lst[i]):
#         pass
#     print(k,v)
#     i-=1
#
#to find the maximum point
print(max(ISL,key=ISL.get))

#to sort the teams based on the rank
print(sorted(ISL,key=ISL.get,reverse=True))