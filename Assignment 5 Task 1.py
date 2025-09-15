# Task 3: Create a Dictionary of Student Marks

# Create a dictionary of students and their marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 75,
    "David": 85,
    "Eve": 79
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display the marks, or show a message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")