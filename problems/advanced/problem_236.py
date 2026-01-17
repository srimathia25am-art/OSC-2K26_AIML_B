"""
Problem 236: Gradebook Application (Class)
Error Type: LOGICAL

Instructions:
This is a practical problem. Read the code and comments to understand the goal.
1. Identify the bug that is causing the incorrect output.
2. Fix the bug.
3. Run the script to ensure it now produces the expected output.

Difficulty: Advanced
"""

# Problem: A Gradebook class that incorrectly calculates the class average.
# Expected Output: "Class Average: 85.0"

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grades):
        self.students[name] = grades

    def get_student_average(self, name):
        grades = self.students.get(name, [])
        return sum(grades) / len(grades) if grades else 0

    def get_class_average(self):
        total_avg = 0
        # Logic error: This calculates the average of averages, which is wrong.
        for name in self.students:
            total_avg += self.get_student_average(name)
        return total_avg / len(self.students) if self.students else 0

book = Gradebook()
book.add_student("Alice", [80, 90]) # Avg 85
book.add_student("Bob", [70, 100]) # Avg 85
print(f"Class Average: {book.get_class_average()}")