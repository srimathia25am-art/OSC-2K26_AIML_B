"""
Problem 97: Email Validator
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: A simple email validator that is too strict.
# Expected Output: True

def is_valid_email(email):
    # This logic is flawed, it doesn't account for subdomains or other characters
    if "@" in email and "." in email.split('@')[1]:
        return True
    return False

print(is_valid_email("test@example.co.uk"))