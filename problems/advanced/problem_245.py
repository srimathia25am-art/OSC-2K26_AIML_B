"""
Problem 245: Simple Bank Account (Class)
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Advanced
"""

# Problem: A BankAccount class that allows overdrafts due to a logic flaw.
# Expected Output: "Error: Insufficient funds."

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance: # Should be <=
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Error: Insufficient funds.")

acc = BankAccount(100)
acc.withdraw(100) # This should be allowed
acc.withdraw(1)   # This should fail
