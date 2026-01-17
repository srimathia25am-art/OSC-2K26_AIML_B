"""
Problem 86: Contact Book Search
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: Search for a contact by name, but the loop returns the wrong one.
# Expected Output: {'name': 'Bob', 'phone': '555-0102'}

contacts = [
    {'name': 'Alice', 'phone': '555-0101'},
    {'name': 'Bob', 'phone': '555-0102'},
]

def find_contact(name):
    for contact in contacts:
        if name in contact['name']:
            return contact # Returns Alice for "Bob" because "b" is not in "Alice"
    return None

found = find_contact("Bob")
print(found)