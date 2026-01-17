"""
Problem 264: Configuration File Parser
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Advanced
"""

# Problem: A script to parse a simple .ini style config file, but it handles sections incorrectly.
# Expected Output: {'user': {'name': 'alice'}, 'database': {'host': 'localhost'}}

config_text = """
[user]
name = alice
[database]
host = localhost
"""
def parse_config(text):
    config = {}
    current_section = None
    for line in text.strip().split('\n'):
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            config[current_section] = {}
        elif '=' in line and current_section:
            key, value = line.split('=', 1)
            # Logical error: assigns to the same dict every time
            config[key.strip()] = value.strip()
    return config

print(parse_config(config_text))