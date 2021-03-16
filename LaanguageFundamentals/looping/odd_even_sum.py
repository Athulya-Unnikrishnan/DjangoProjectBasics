i=1
n=int(input("Enter a limit"))
sumodd=0
sumeven=0
counteven=0
countodd=0

while(i<=n):
    if(i%2==0):
        counteven += 1
        sumeven+=i
    else:
        countodd+=1
        sumodd+=i
    i+=1
print("even sum",sumeven)
print("count of even ",counteven)
print("odd sum",sumodd)
print("count of odd",countodd)