# =====================================================
#                ENCAPSULATION
# =====================================================
# A bank account should protect its balance.
# Nobody should directly modify the balance.
# The balance can only be changed using methods.
# =====================================================

class BankAccount:

    # Constructor
    def __init__(self, balance):
        self.__balance = balance     # Private variable

    # Deposit money
    def deposit(self, amount):
        self.__balance += amount
        print(amount, "Tk deposited.")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, "Tk withdrawn.")
        else:
            print("Insufficient balance.")

    # Check balance
    def get_balance(self):
        return self.__balance


# Creating object
acc1 = BankAccount(5000)

# Accessing through methods
acc1.deposit(2000)
acc1.withdraw(1500)

print("Current Balance:", acc1.get_balance())