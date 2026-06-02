#ques:1 print numbers from 1 to 100
#print numbers from 100 to 1
#print the multiiplication table of a number n
#print the elements of the following list
#[1,4,9,16,25,36,64,81,100]
#search for a number x in this tuple using loops
#(1,4,9,16,25,36,49,64,81,100)

#ques-1:
i=1
while i<=100:
    print(i)
    i+=1
#ques-2
p=100
while p>=1:
    print(p)
    p-=1

#ques-3
n=int(input("enter a number: "))
j=1
while j<=10:
    p=n*j
    print(n,'X',j,'=',p)
    j+=1

#ques-4
nums=[1,4,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1

#ques-5
tuple=(1,4,9,16,25,36,49,64,81,100)
x=25
id=0
while id<len(tuple):
    if(x==tuple[id]):
        print('found the number x',tuple[id])
    id+=1