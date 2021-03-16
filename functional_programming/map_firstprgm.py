
lst=[1,2,3,4,5,6,7,8,9]

# def square(num):
#     return num**2

#instead of using the square function we can use lambda function

# sq=lambda num:num**2

#instead of using lamda and storing into a variable we can do that in one single line
#syntax of map is map(function name, iteratable list)
#sq=list(map(square,lst))
#we are converting the map to list because map will return map reference value so we convert them to list
#and store the values in list



sq=list(map(lambda num:num**2,lst))
print(sq)