
score = float(input("Enter the student's score (0-100): "))


if 80 <= score <= 100:
    grade = "A"
elif 61 <= score <= 79:
    grade = "B"
elif 41 <= score <= 60:
    grade = "C"
elif 21 <= score <= 40:
    grade = "D"
elif 0 <= score <= 20:
    grade = "F"
else:
    grade = "Invalid score"


print(f"The student's grade is: {grade}")