"""
Problem 51: Student Grade Calculator
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: Calculate a student's final grade, but the grading scale is wrong.
# Expected Output: "Grade: B"

scores = [85, 90, 88, 92]
average = sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg > 80: # Should be >= 80
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "F"

grade = get_grade(average)
print(f"Grade: {grade}")