"""
Problem 268: Hangman Game Logic
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Advanced
"""

# Problem: The core logic for a Hangman game that doesn't reveal all instances of a letter.
# Expected Output: "_pp_e"

secret_word = "apple"
guessed_letters = ['p', 'e']
display = ""

for letter in secret_word:
    if letter in guessed_letters:
        display += letter
    else:
        display += "_"
# The loop is fine, but let's introduce a common mistake in game logic
# For example, what if we only replace the *first* instance?
display_word = "_" * len(secret_word)
for letter in guessed_letters:
    if letter in secret_word:
        index = secret_word.find(letter)
        display_word = display_word[:index] + letter + display_word[index+1:]

print(display_word) # This logic is flawed for repeated letters
