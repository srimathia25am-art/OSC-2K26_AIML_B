"""
Problem 55: To-Do List
Error Type: VALUE_ERROR

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: Remove an item from a to-do list, but the item doesn't exist.
# Expected Output: Should handle the error, e.g., print "Item not found."

todo_list = ["laundry", "dishes", "shopping"]

def remove_item(item):
    todo_list.remove(item) # Raises ValueError if item is not in list
    print(f"Removed '{item}'")

remove_item("coding")
print(todo_list)