# TASK 1.Create a class called BankAccount with the attributes: - account number , balance , owner name , date opened 
# 2.Add some behaviour to the above class using the methods: - deposit() - withdraw() -display_info()
# 3.Create 2 BankAccount objects that can deposit , withdraw and display amount

class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number =account_number
        self.balance = balance
        self.owner_name =owner_name
        self.date_opened = date_opened
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount     
        else:
            print("Invalid amount. Please enter a positive number.")    
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")

account1 = BankAccount("ABD-123-2026",0,"Hillary","2026-02-18")
account2 = BankAccount("ABD-456-2026",0,"Job","2026-02-18")
account1.display_info()
account1.deposit(10000)
account1.withdraw(5000)
account1.display_info()
account2.display_info()
account2.deposit(15000)
account2.withdraw(3000)
account2.display_info()
