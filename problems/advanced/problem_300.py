"""
Problem 300: JSON Data Processor
Error Type: TYPE_ERROR

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Advanced
"""

# Problem: Read JSON data from a file and process it, but assume a wrong data structure.
# Expected Output: "Processed 2 records."

import json

# Assume data.json contains: {"records": [{"id": 1}, {"id": 2}]}
json_data = '{"records": [{"id": 1}, {"id": 2}]}'
with open("data.json", "w") as f:
    f.write(json_data)

def process_records(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        # TypeError: 'dict' object is not iterable. Should be data['records']
        for record in data:
            print(f"Processing record id: {record['id']}")
    print(f"Processed {len(data)} records.")

process_records("data.json")
os.remove("data.json")