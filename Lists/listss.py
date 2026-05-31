marks = [94.4,87.5,95.4,45.1,66.4]
print(marks)
print(type(marks))
print(marks[2])
print(len(marks)) #length of the lists
#we can store diff types element such as integer,float,string together
student=['karan',22,85.5,'bd']
print(student)
#strings are immutable but lists are mutable
#mutable means we can change ,immutabe means we cant change after assign
#example
student[0]='mina'
print(student)
#slicing in lists
print(student[1:3])
print(student[:3])#python automatic assign the starting or ending index if we dont give
print(student[2:])

#List methods
list=[2,1,3]
list.append(4) #adds one element at the end
print(list)
list.sort() #sort in ascending order
print(list)
list.sort(reverse=True) #descending order
print(list)
list.reverse() #reverse a list
print(list)
list.insert(2,7) #insert a value in a index,2 is the index here,7 is the value we want to insert
print(list)
list.remove(1) #removes the first occurance of elements
print(list)
list.pop(3) #removes elements at index
print(list)
my_list=[1,2,3,4,5]
copied_list=my_list.copy()#give the copy of one lists
print(copied_list)
my_list=[1,2,2,3,4,5,6]
print(my_list.count(2)) #count the occurance of the particular elements
