"""
Problem 69: File Word Counter
Error Type: FILE_NOT_FOUND

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Medium
"""

# Problem: Read a file and count words, but the file path is wrong.
# Expected Output: Should handle the FileNotFoundError.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as f:
            words = f.read().split()
            print(f"Word count: {len(words)}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

count_words_in_file("data.txt") # Assumes this file doesn't exist
