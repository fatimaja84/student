from Student.grades import avg, max_grade, min_grade
from Student.status import check_status


name = input("Enter student name: ")

while name == "":
    print("Please enter a name.")
    name = input("Enter student name: ")

while True:
    try:
        count = int(input("How many grades? "))
        if count > 0:
            break
        print("Enter a number greater than zero.")
    except ValueError:
        print("Please enter a whole number.")

grades = []

for i in range(count):
    while True:
        try:
            grade = float(input("Enter grade " + str(i + 1) + " (0 to 20): "))
            if 0 <= grade <= 20:
                grades.append(grade)
                break
            print("Grade must be between 0 and 20.")
        except ValueError:
            print("Please enter a number.")

average = avg(grades)
highest = max_grade(grades)
lowest = min_grade(grades)
result = check_status(average)

print("----------------------")
print("Student:", name)
print("Avg =", round(average, 2))
print("Max =", highest)
print("Min =", lowest)
print("Status =", result)
