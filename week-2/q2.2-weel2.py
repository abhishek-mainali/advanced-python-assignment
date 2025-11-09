# 1. Employee Salaries
employees = {
    "John": 55000,
    "Emma": 62000,
    "Raj": 75000,
    "Lina": 48000
}

filtered = filter(lambda item: item[1] >= 60000, employees.items())
raised = list(map(lambda item: (item[0], item[1] * 1.05), filtered))
print("Updated Salaries:", raised)


# 2. Exam Scores to Grades
scores = [95, 82, 67, 45, 78, 54, 89, 90]

passed = filter(lambda s: s >= 50, scores)
grades = list(map(lambda s: 
    'A' if s >= 90 else 
    'B' if s >= 80 else 
    'C' if s >= 70 else 
    'D' if s >= 60 else 
    'E', passed))
print("Grades:", grades)
