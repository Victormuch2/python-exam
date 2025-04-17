class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depositing {amount}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawing {amount}")
        else:
            print("Withdrawal amount must be positive")
    
    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

#examples
account = BankAccount("123456789")  
account.deposit(5000)               
account.withdraw(2000)              
account.get_balance()              
