student_name = input()
gpa = float(input())
credit_hours = int(input())

if gpa >= 3.8 and credit_hours >= 12:
    classification = "Dean's List"
elif gpa >= 3.5 and credit_hours >= 12:
    classification = "Honor Roll"
elif gpa >= 2.0:
    classification = "Good Standing"
else:
    classification = "Academic Probation"

print(classification)
