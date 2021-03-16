#args will accept n number of arguments
def add(*args):
    sum = 0
    print(args)#stores values in tuple format
    for a in args:
        #print(a)
        sum+=a
    print(sum)
add(10,20,30,40)

#"*args" cannot accept the values as key value pair so to remove the drawback of *args we use **args and it will accept the data in dictionary format so we names them as **kwargs

def add(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

add(eid=100,Job="Kakkanad",Resid="Thrissur")