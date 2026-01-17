"""
Problem 182: Simple ATM
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: A simple ATM withdrawal function with a logic flaw.
# Expected Output: "Withdrawal successful. New balance: 50"

balance = 100

def withdraw(amount):
    global balance
    if balance > amount: # Should be balance >= amount
        balance -= amount
        print(f"Withdrawal successful. New balance: {balance}")
    else:
        print("Insufficient funds.")

withdraw(100)