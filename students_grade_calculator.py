def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_result(name, marks):
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    print("\n========== RESULT ==========")
    print(f"Student Name : {name}")
    print(f"Marks        : {marks}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")

    if grade == "F":
        print("Status       : Failed ❌")
    else:
        print("Status       : Passed ✅")


def main():
    print("🎓 Student Grade Calculator")

    name = input("Enter student name: ")

    marks = []

    subjects = ["Python", "DSA", "DBMS", "Mathematics", "Computer Networks"]

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    display_result(name, marks)


main()