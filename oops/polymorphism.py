#when the same operator is allowed to have different meaning according to the context
print(1+2) #sum
print("Fatema"+"SWE") #concat
print([1,2,3]+[4,5,6]) #merge
#polymorhism:operator overloading
 
class Complex:
    def __init__(self,real,img):
        self.real=real 
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    # def add(self,num2):
    #     newReal=self.real+num2.real
    #     newImg = self.img+num2.img
    #     return Complex(newReal,newImg) 
            
    def __add__(self,num2):#for directly adding
        newReal=self.real+num2.real
        newImg = self.img+num2.img
        return Complex(newReal,newImg)         

num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(4,6)
num2.showNumber()
#  num3=num1+num2 give the error,we cant do it directly

# num3 = num1.add(num2)
# num3.showNumber()
#now can directly add 
num4 = num1+num2
num4.showNumber()
# =====================================================
#               POLYMORPHISM IN PYTHON
# =====================================================
# Definition:
# Polymorphism means "One thing, many forms."
# The same operator or function can perform different
# tasks depending on the data type.
# =====================================================

# Integer Addition
print(1 + 2)                 # Output: 3

# String Concatenation
print("Fatema" + "SWE")      # Output: FatemaSWE

# List Merging
print([1, 2, 3] + [4, 5, 6]) # Output: [1,2,3,4,5,6]


# =====================================================
#              OPERATOR OVERLOADING
# =====================================================
# Python allows us to change the behavior of operators
# for user-defined classes.
#
# Example:
# + operator works differently for:
#   int    -> Addition
#   string -> Concatenation
#   list   -> Merge
#
# We can also make + work for our own class.
# =====================================================


class Complex:

    # Constructor
    def __init__(self, real, img):
        self.real = real
        self.img = img

    # Display Complex Number
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    # Operator Overloading (+)
    # num1 + num2
    # Python internally calls:
    # num1.__add__(num2)
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img

        # Returning a new Complex object
        return Complex(newReal, newImg)


# =====================================================
#               Creating Objects
# =====================================================

num1 = Complex(1, 3)
num2 = Complex(4, 6)

print("First Complex Number:")
num1.showNumber()

print("Second Complex Number:")
num2.showNumber()


# =====================================================
# Without Operator Overloading:
#
# num3 = num1.add(num2)
#
# With Operator Overloading:
#
# num3 = num1 + num2
#
# Python internally does:
# num1.__add__(num2)
# =====================================================

num3 = num1 + num2

print("After Addition:")
num3.showNumber()


# =====================================================
# Output:
#
# 3
# FatemaSWE
# [1, 2, 3, 4, 5, 6]
#
# First Complex Number:
# 1 i + 3 j
#
# Second Complex Number:
# 4 i + 6 j
#
# After Addition:
# 5 i + 9 j
# =====================================================


# Important Magic Methods:
#
# +   --> __add__()
# -   --> __sub__()
# *   --> __mul__()
# /   --> __truediv__()
# ==  --> __eq__()
# <   --> __lt__()
# >   --> __gt__()
#
# These are called Magic Methods or Dunder Methods.
# =====================================================
