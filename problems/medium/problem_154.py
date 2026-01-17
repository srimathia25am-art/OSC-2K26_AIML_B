"""
Problem 154: Word Counter
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: Count word frequencies in a text, but it's case-sensitive.
# Expected Output: {'hello': 2, 'world': 1}

text = "Hello hello world"
word_counts = {}
for word in text.split():
    # This logic is case-sensitive
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)