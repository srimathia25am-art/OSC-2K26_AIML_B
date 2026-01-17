"""
Problem 63: Password Strength Checker
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: A password checker that miscalculates the score.
# Expected Output: "Strength: Medium"

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    
    # Logic error in score interpretation
    if score == 3:
        return "Strong"
    elif score == 2:
        return "Weak" # Should be Medium
    else:
        return "Medium" # Should be Weak

print(f"Strength: {check_password_strength('Password123')}")