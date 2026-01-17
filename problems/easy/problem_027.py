"""
Problem 27: List Reverser
Error Type: ATTRIBUTE

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Easy
"""

# Problem: Reverse a list, but call a non-existent method.
# Expected Output: [3, 2, 1]

my_list = [1, 2, 3]
my_list.revers() # Typo in method name
print(my_list)