# 6. Student Grade Report
# Concepts: list of tuples, tuple unpacking, for, if/elif grading, max/min by manual
# tracking
# Start with:
# students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
# Print each student's letter grade (A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F). Then print
# the class average and the top and bottom scorers. Find the top and bottom scorers with
# a loop, not with max() and a key.



students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total = 0

top_name, top_marks = students[0]
bottom_name, bottom_marks = students[0]

for name, marks in students:
    # Calculate letter grade
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(name, ":", marks, "-", grade)

    total += marks
    if marks > top_marks:
        top_name = name
        top_marks = marks
    if marks < bottom_marks:
        bottom_name = name
        bottom_marks = marks

average = total / len(students)

print("Class average:", average)
print("Top scorer:", top_name, "-", top_marks)
print("Bottom scorer:", bottom_name, "-", bottom_marks)