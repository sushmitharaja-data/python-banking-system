# Python Banking System

## Internship
**Organization:** Codomax Digital Solutions  
**Module:** Module 3 – Object-Oriented Python  
**Days:** Day 11 – Day 15  
**Project:** Python Banking System

## 1. Project Overview
The Python Banking System is a menu-driven application developed using Object-Oriented Programming concepts. It allows users to create bank accounts, deposit money, withdraw money, view account details, and check transaction history.

## 2. Objectives
- Understand classes and objects.
- Implement constructors and methods.
- Demonstrate encapsulation, inheritance, polymorphism, and abstraction.
- Maintain transaction history for each account.
- Develop a structured and reusable Python application.

## 3. Technologies Used
- Python 3
- Python IDLE
- Object-Oriented Programming

## 4. Features
1. Create Savings and Current accounts.
2. Deposit money.
3. Withdraw money.
4. View account details and balance.
5. View transaction history.
6. Validate invalid amounts and account numbers.

## 5. OOP Concepts
- **Class:** `BankAccount`, `SavingsAccount`, and `CurrentAccount`.
- **Object:** Individual account objects created at runtime.
- **Constructor:** `__init__()` initializes account details.
- **Encapsulation:** The balance is stored in the private attribute `__balance`.
- **Inheritance:** Savings and Current accounts inherit from `BankAccount`.
- **Polymorphism:** Each account type provides its own `account_type()` method.
- **Abstraction:** The abstract `BankAccount` class defines the required account type method.

## 6. How to Run
1. Install Python 3.
2. Open `banking_system.py` using Python IDLE.
3. Press F5 to run the program.
4. Follow the menu options displayed in the Shell.

## 7. Testing
Test account creation, deposits, withdrawals, balance display, transaction history, invalid amounts, and insufficient balance.

## 8. Limitations
Account data is stored in memory and is lost when the program exits. This is a learning project and is not intended for real banking transactions.

## 9. Conclusion
This project demonstrates the practical application of Python OOP concepts by implementing a simple banking workflow with account management and transaction history.
