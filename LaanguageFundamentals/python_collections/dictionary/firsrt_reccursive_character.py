# alphabet_str=["A", "A", "C","C"]
# for i in alphabet_str:
#     print(i)
#     for j in alphabet_str:
#         print(i,j)
#         if(i==j):
#             break
#         print(i," is the first recursive character")
alpha="BACCB"
dict={}
for a in alpha:
    if a not in dict:
        dict[a]=1
    else:
        print("first recurssive character is",a)
        break