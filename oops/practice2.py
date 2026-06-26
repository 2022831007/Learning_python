#create an account class with 2 attributes -balance and account no
#create methods for debt,credit&printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.acc=acc
  #debit method
    def debit(self,amount):
     self.balance-=amount
     print("Rs.",amount,"was debited")
     print("total balance = ",self.get_balance())
    #credit method
    def credit(self,amount):
     self.balance+=amount
     print("Rs.",amount,"was credited") 
     print("total balance = ",self.get_balance())
    def  get_balance(self):
       return self.balance

acc1 = Account(10000,12345)  
print(acc1.balance)
acc1.debit(1000)
print(acc1.acc)      
acc1.credit(500)
acc1.debit(200)
acc1.credit(4000)