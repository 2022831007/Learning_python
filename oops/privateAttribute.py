class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #make it private attribute,we cant access outside the class
    def reset_pass(self): #access the private attribute with this method
        print(self.__acc_pass)



acc1 = Account("1234","abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass) #it will give the error,as it is private
print(acc1.reset_pass())


