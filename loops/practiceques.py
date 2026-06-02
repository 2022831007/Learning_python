#to find the sum of  first n numbers (using while)
n= int(input('enter a number : '))
i=1
sum=0
while i<=n:
   sum+=i
   i+=1

print(sum)
#using for
sum1=0
for id in range(1,n+1):
   sum1+=id

print(sum1)
#find the factorial of first n numbers(using for)
fact=1
for idx in range(1,n+1):
   fact*=idx
idx+=1


print(fact)
