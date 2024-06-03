class Account:
    def __init__(self,number,pin,withdraw,deposit):
        self.number = number
        self. __pin = pin
        self. __balance = 0
        self.

    def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "wrong pin"

    def deposit(self):
        amount=float(input("Enter your deposited amount: "))
        self.balance += amount
        print("\n amount has Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)def cleanUp(self, pin, account_transfer):
        if pin == self.__pin:
            return f"Your account balance of {self.__balance} has been successfully transferred to {account_transfer} account"
        else:
            return "Wrong pin"
def close_account(self, pin, account_number):
        if pin == self.__pin:
            for account in self.accounts_lists:
                if account_number == account.account_number:  
                    self.accounts_lists.remove(account)
                    return f"This {account_number} account has been successfully removed"
            return "The account number does not exist in the accounts list"
        else:
            return "Wrong pin"

    
 