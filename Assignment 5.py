#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import time

class Account:
    def __init__(self, account_type, name="", company_name="", initial_balance=0):
        self.account_type = account_type
        self.name = name
        self.company_name = company_name
        self.balance = initial_balance
        self.account_number = self.generate_account_number()

        self.transactions = []

    def generate_account_number(self):
            return random.randint(0000000000,99999999999)


    def deposit(self, amount):
        self.balance += amount
        self.log_transaction("Deposit", amount)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Low Balance.")
            return False

        self.balance -= amount
        self.log_transaction("Withdrawal", amount)
        return True

    def log_transaction(self, transaction_type, amount):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": timestamp
        })

class SavingsAccount(Account):
    def __init__(self, name="", initial_balance=0):
        super().__init__("Savings", name=name, initial_balance=initial_balance)

class CurrentAccount(Account):
    def __init__(self, company_name="", initial_balance=0):
        super().__init__("Current", company_name=company_name, initial_balance=initial_balance)

if __name__ == "__main__":
    def get_positive_float_input(prompt):
        for i in range(3):
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("Initial balance must be greater than or equal to zero.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("Maximum number of attempts reached. Exiting program.")
        exit()

    account_type = input("Enter account type (Savings/Current): ").strip().lower()

    if account_type == "savings":
        name = input("Enter application name: ")
        initial_balance = get_positive_float_input("Enter initial balance (default is 0): ")
        account = SavingsAccount(name=name, initial_balance=initial_balance)
    elif account_type == "current":
        company_name = input("Enter company name: ")
        initial_balance = get_positive_float_input("Enter initial balance: ")
        account = CurrentAccount(company_name=company_name, initial_balance=initial_balance)
    else:
        print("Invalid account type. Exiting program.")
        exit()

    print("Account created.")
    print(f"Account type: {account.account_type}")
    print(f"Account number: {account.account_number}")
    print(f"Initial balance: {account.balance}")

    while True:
        action = input("Enter action (deposit/withdraw/exit): ").strip().lower()

        if action == "deposit":
            amount = get_positive_float_input("Enter deposit amount: ")
            account.deposit(amount)
            print(f"New balance: {account.balance}")
        elif action == "withdraw":
            amount = get_positive_float_input("Enter withdrawal amount: ")
            success = account.withdraw(amount)
            if success:
                print(f"New balance: {account.balance}")
        elif action == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid action.")




# In[ ]:




