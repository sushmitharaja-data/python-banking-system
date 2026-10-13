
# Codomax Internship - Module 3
# Python Banking System
# OOP Concepts and Transaction History

from abc import ABC, abstractmethod
from datetime import datetime


class BankAccount(ABC):
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.transactions = []
        self.transactions.append(
            f"{datetime.now():%Y-%m-%d %H:%M} | Account created | Balance: Rs.{balance:.2f}"
        )

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a deposit amount greater than zero.")
            return
        self.__balance += amount
        self.transactions.append(
            f"{datetime.now():%Y-%m-%d %H:%M} | Deposit | Rs.{amount:.2f}"
        )
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a withdrawal amount greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            self.transactions.append(
                f"{datetime.now():%Y-%m-%d %H:%M} | Withdrawal | Rs.{amount:.2f}"
            )
            print("Withdrawal successful.")

    @abstractmethod
    def account_type(self):
        pass

    def show_details(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type())
        print("Balance: Rs.", format(self.balance, ".2f"))

    def show_history(self):
        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"


class CurrentAccount(BankAccount):
    def account_type(self):
        return "Current Account"


def main():
    accounts = {}

    while True:
        print("\n===== PYTHON BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account Details")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ").strip()
            number = input("Create account number: ").strip()

            if not name or not number:
                print("Name and account number cannot be empty.")
            elif number in accounts:
                print("Account number already exists.")
            else:
                print("1. Savings Account")
                print("2. Current Account")
                kind = input("Choose account type: ")

                if kind == "1":
                    accounts[number] = SavingsAccount(name, number)
                elif kind == "2":
                    accounts[number] = CurrentAccount(name, number)
                else:
                    print("Invalid account type.")
                    continue

                print("Account created successfully!")

        elif choice in ("2", "3", "4", "5"):
            number = input("Enter account number: ")
            account = accounts.get(number)

            if account is None:
                print("Account not found. Create an account first.")
                continue

            if choice == "2":
                try:
                    account.deposit(float(input("Enter deposit amount: Rs.")))
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                try:
                    account.withdraw(float(input("Enter withdrawal amount: Rs.")))
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                account.show_details()
            elif choice == "5":
                account.show_history()

        elif choice == "6":
            print("Thank you for using Python Banking System!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
