#to check if a number enterd by users is odd or even
num=int(input("enter a number"))
if(num%2==0):
    print("the number is even")

else:
    print("the number is odd")


#ques-2:to find the greatest of 3 numbers enterd by users
num1=int(input("enter a number1 : "))
num2=int(input("enter a number2 : "))
num3=int(input("enter a number3 : "))
if(num1>num2 and num1>num3):
    print("num1 is the greatest")

elif(num2>num1 and num2>num3):
    print("num2 is the greatest")

else:
    print("num3 is the greatest")

#ques-3:to check if the number is multiple of 7 or not
num4=int(input("enter a number: "))
if(num4%7==0):
    print("number is multiple of 7")

else:
    print("not multiple of 7")