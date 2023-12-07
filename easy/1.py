#str="Hello World"
str=input()# we will take input  string  and keep here
str=str.split() #then we will convert it into array using split method based on space as seperator.
print(len(str[-1])) # since the last element will be the last word after the last space we are printing it by accessing it using -1