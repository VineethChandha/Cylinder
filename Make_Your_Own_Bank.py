#PY.01.18 Project 10: Make your own bank
#Description: It uses oops concepts to create a savings and current account and carries the transactions.

class Account:                      #Super Class
    def __init__(self, name, balance, min_balance):     #Constructor        Self is bacisally referces to the current instances(object)
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance +=  amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))

class Current(Account):                 #Inheritance of parent class
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000 )  #Connecting with super class     

    def __str__(self):                          #this is used to get correct format answer for print(Z) or T
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance)

class Savings(Account):             #Inheritance of parent class
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance)

    
Z=Current("Vinnu",500)
print(Z)
Z.deposit(300)
Z.statement()
Z.withdraw(1000)
Z.statement()
Z.withdraw(800)
Z.statement()
Z.withdraw(1)
print(Z)

T=Savings("Vinnu",500)
print(T)
T.deposit(300)
T.statement()
T.withdraw(1000)
T.statement()
T.withdraw(800)
T.statement()
T.withdraw(1)
print(T)
