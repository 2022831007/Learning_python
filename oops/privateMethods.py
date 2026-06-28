class Person:
    __name="anynomous" #private attributes

    def __hello(self):#private method
        print("hello person!")

    def welcome(self):#to access the private method
        self.__hello()


p1 = Person()
# print(p1.__hello()) #as private method,it will give error,as it it is outside the class
print(p1.welcome())