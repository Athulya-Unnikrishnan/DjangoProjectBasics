list1=[10,20,23,26]
position=int(input("Enter the position whose value you need to see"))

try:
    print(list1[position])
# except:
#     print("Index out of range exception occured")
#
#to see which error occured we can use Exception class
#that is except Exception as e:

# except Exception as e:
#     print(e.args)

#instead of showing the error message we can write code inside the except method to sove the exception
except Exception as e:
    print("enter valid index")
    position = int(input("Enter the position whose value you need to see"))
    print(print(list1[position]))