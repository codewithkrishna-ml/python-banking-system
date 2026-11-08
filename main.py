#PROJECT- BANKING SYSTEM
class BankAccount:
    def __init__(self , account_holder , balance , pin):
        self.account_holder = account_holder
        self.__balance = balance
        self.__pin = pin

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposit successfully")
        else:
            print("Error: Amount must be greater than 0")

    def withdraw(self, amount , entered_pin):
        if entered_pin == self.__pin and amount <=self.__balance:
            self.__balance -= amount
            print(f"{amount} withdraw successfully")
        else:
            print("Error: Invailed pin! Cannot fetch balance")

    def get_balance(self , entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        else:
            print("Error: Invailed pin! Cannot fetch balance")
            return None
             
        

my_account = BankAccount("krishna" , 1000 , "1234")

my_account.__balance = 500000

my_account.deposit(500)

print("Current balance:" , my_account.get_balance("1234"))