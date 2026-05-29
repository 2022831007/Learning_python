#type conversion,python authomatic does this
a=2
b=4.25

sum=a+b
print(sum) #python automatic convert the int to float,as float is superior
#type casting as python cant automatic convert string to int or int to sting and  cant do operation with int and string together 
c,d=1,"2"
d=int("2")
print(c+d)
# convert to string
a=3.14
a=str(a)
print(type(a))