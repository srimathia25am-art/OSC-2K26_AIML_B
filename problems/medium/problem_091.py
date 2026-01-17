"""
Problem 91: Simple Inventory Manager
Error Type: KEY_ERROR

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: Update an item count in an inventory, but the item doesn't exist.
# Expected Output: Should handle the missing item gracefully, e.g., by adding it.

inventory = {"apples": 10, "bananas": 20}

def update_stock(item, quantity):
    inventory[item] += quantity # Fails if item is not in inventory
    print(f"Updated {item} to {inventory[item]}")

update_stock("oranges", 5)
print(inventory)