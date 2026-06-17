#WAF to print the length of a list(list in the parameter)
num = [4,5,6,7]
nm2 = [2,3,4,5,6,7,8]
def print_len(list):
    print(len(list))


     
print_len(num)
print_len(nm2)

#write a function to print the elements of a list in a single line
def print_el(list):
    for i in list:
        print(i,end=" ")


print_el(nm2)
print() #to remove the percentage in the last
    
#WAF to find the factorial of n (n is the parameter)   
def cal_fact(n):
     fact=1
     for i in range(1,n+1):
         fact*=i
     print(fact)      

cal_fact(5)
#WAF to convert USD to Taka
def converter(usd_val):
    taka_val= usd_val*122.82
    print(usd_val,"USD = ",taka_val,"Taka")


converter(2)

#write a function which take input and give the output if a number is odd print odd string or even
nums= int(input("enter a number"))
def oddEven(n):
    if(n%2!=0):
        print("Odd")
    else:
     print("even")  

oddEven(nums)


