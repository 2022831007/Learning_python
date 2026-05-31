#Ques-1:to ask user to enter name of their 3 favourite movies &store them in a list
movies=[]
mov1=input("eneter 1st movie: ")
mov2=input("eneter 2nd movie: ")
mov3=input("eneter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#another way
n=int(input("how many movies:"))
list=[]
for i  in range(n):
    mov=input("give the movie name : ")
    list.append(mov)

print(list)

#Ques-2:to check a list contains palindrome of elemenets
[1,2,3,2,1] [1,"abc","abc",1]
list1=[1,2,3,2,1]
list2=list1.copy()
list2.reverse()
if(list1==list2):
    print("yes,palindrom")


else:
    print("not palindrome")

#ques-3:to count the number of stundents with "A" grade in the following tupple
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
#ques-4:store the values in lists and sort them from "A" to "D"
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)