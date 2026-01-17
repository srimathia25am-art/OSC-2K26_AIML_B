"""
Problem 58: Dice Rolling Simulator
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: Simulate rolling two dice, but the range of numbers is incorrect.
# Expected Output: A number between 2 and 12.

import random

def roll_dice():
    die1 = random.randint(1, 7) # Incorrect upper bound
    die2 = random.randint(1, 6)
    return die1 + die2

print(f"You rolled a {roll_dice()}")