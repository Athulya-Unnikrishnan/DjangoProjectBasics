
try:
    num = int(input("Enter a number"))
    print(num)
    if(num<0):
        raise Exception("number less than 0")
except Exception as e:
    print("Enter a number greater than 0")
    num=int(input("Enter a number"))
    print(num)