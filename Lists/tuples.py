#a built in data-types that lets us create immutable sequence of values
#list-mutable,tuple-immutable,string-immutable
tuple=(2,3,4,5)
print(tuple)
print(type(tuple))
print(tuple[2]) #print specific value of tuple
# tuple[0]=5 ,it will give error,as tuplle is immutable,we cant assign  
tup=() #empty tuple
print(tup)
print(type(tup))
tup=(1)
print(type(tup)) #python will think it as int ,return int 
tup=(1,)
print(type(tup)) # as we give the comma after 1,now python give the output as tuple 
#slicing in tuple
print(tuple[1:3])
print(tuple[:3])
print(tuple[2:])

#tuple methods
print(tuple.index(3)) #to find the specific element of a index,here 3 is the element and it will return the index 

print(tuple.count(2)) #count the occurance of a element in a tuple
