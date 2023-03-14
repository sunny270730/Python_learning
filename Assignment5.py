import random
from abc import ABC, abstractmethod
import os

class Account(ABC):
    def __init__(self):
        pass
            
    def add_log(self, transaction_type, amount):
        transaction = {"Transaction Type": transaction_type, "Amount": amount}
        self.transactions.append(transaction)
        self.transaction_count += 1
        if self.transaction_count > 5:
            print("Transaction limit exceeded. Rs. 10 will be charged for every additional transaction.")
            self.deduct_charge()

    def deduct_charge(self):
        self.balance -= 10


    @abstractmethod
    def withdraw(self, amount):

        if amount > 0:
            if amount % 100 != 0:
                print("Amount multiple of 100.")
            elif amount > 10000:
                print("withdraw amount")
            elif self.balance - amount < self.min_balance:
                print(f"Minimum balance of Rs. {self.min_balance} should be maintained.")
            else:
                self.balance -= amount
                self.add_log("Debit", amount)
                print(f"Rs. {amount} has been withdrawn from your account.")
        
        else:
            print('withdraw amount not a valid')
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_log("Credit", amount)
            print(f"deposite amount {amount} is  ")
    
    def get_statement(self):
        for transaction in self.transactions:
            print(f"{transaction['Transaction Type']} of Rs. {transaction['Amount']}")
       
   
    def get_account_info(self):
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: {self.balance}")

    
    def balance_enquiry(self):
        print(f"Your current balance is Rs. {self.balance}")

class SavingsAccount(Account):
    def __init__(self):
        self.account_type = "Saving"
        self.name = name
        initial_balance = float(input("Enter initial balance: "))
        self.balance = initial_balance
        self.min_balance = 0 if account_type == "Savings" else 1000
        self.account_number = random.randint(1000000000000000, 9999999999999999)
        self.transactions = []
        self.transaction_count = 0
    def withdraw(self, amount):
        return super().withdraw(amount)
    def deposit(self, amount):
        return super().deposit(amount)    
    
    def get_account_info(self):
        return super().get_account_info()
    def balance_enquiry(self):
        return super().balance_enquiry()
    def deduct_charge(self):
        return super().deduct_charge()
    def __str__(self):
        return f'Account type :- {self.account_type}\n Account Number :- {self.account_number}\n Name :- {self.name}\n Balance :- {self.balance}'

class CurrentAccount(Account):
    def __init__(self):
        self.account_type = "Current"
        self.name = name
        initial_balance = float(input("Enter initial balance: "))
        self.balance = initial_balance
        self.min_balance = 0 if account_type == "Current" else 1000
        self.account_number = random.randint(1000000000000000, 9999999999999999)
        self.transactions = []
        self.transaction_count = 0
    def withdraw(self, amount):
        return super().withdraw(amount)
    def deposit(self, amount):
        return super().deposit(amount)
    def get_account_info(self):
        return super().get_account_info()
    def balance_enquiry(self):
        return super().balance_enquiry()
    def deduct_charge(self):
        return super().deduct_charge()
    def __str__(self):
        return f'Account type {self.account_type}\n Account Number {self.account_number}\n Name {self.name}\n Balance {self.balance}'
    
    def greet():
        name = input("Enter your company name: ")
        print(f"Welcome to our bank, {name}!")
        return name



account_type = int(input("Enter account type:\n1. Savings Account\n2. Current Account\n"))
name = input("Enter Account holder name : ")
if account_type == 1:
    account = SavingsAccount()
    print(f"Savings account created successfully. Account number: {account.account_number}")
elif account_type == 2:
    account = CurrentAccount()
    print(f"Current account created successfully. Account number: {account.account_number}")
else:
    print("Invalid account type selected. Exiting program.")
    exit()


filepath = os.path.join(f"C:\\Users\\sunny\\OneDrive\\Desktop\\Python file\\BankingDetail\\{account.account_number}.txt")
if os.path.isfile(filepath):
    print('File with same name already exist')
else:
    with open(f"C:\\Users\\sunny\\OneDrive\\Desktop\\Python file\\BankingDetail\\{account.account_number}.txt", 'w') as file:
        file.write(str(account) + "\n")

while True:
        choice = int(input("\nEnter choice:\n1. Withdraw\n2. Deposit\n3. Get Statement\n4. Get Account Info\n5. Balance Enquiry\n6. Exit\n"))
        if choice == 1:
            amount = int(input("Enter amount to withdraw (multiple of 100): "))
            account.withdraw(amount)
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 3:
            account.get_statement()
        elif choice == 4:
            account.get_account_info()
        elif choice == 5:
            account.balance_enquiry()
        elif choice == 6:
            print("Thank you for banking with us!")
            exit()
        else:
            print("Invalid choice. Please try again.")


      
