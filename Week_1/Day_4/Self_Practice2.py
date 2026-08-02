#Create a program that stores student grades in a dictionary and calculates the average grade
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96
}

# Calculate the average grade
average_grade = sum(student_grades.values()) / len(student_grades)
print("Average Grade:", average_grade)