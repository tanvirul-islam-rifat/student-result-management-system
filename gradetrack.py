"""
GradeTrack - Student Result Management System
A simple CLI application to manage student records, calculate grades,
and store/retrieve data using file handling.

Course: CSE110 - Programming Language I
"""

import os

DATA_FILE = "data/students.txt"


# ---------- Grade Calculation ----------
def calculate_grade(marks):
    """Convert numeric marks (out of 100) into a letter grade and grade point."""
    if marks >= 90:
        return "A+", 4.00
    elif marks >= 85:
        return "A", 4.00
    elif marks >= 80:
        return "A-", 3.70
    elif marks >= 75:
        return "B+", 3.30
    elif marks >= 70:
        return "B", 3.00
    elif marks >= 65:
        return "B-", 2.70
    elif marks >= 60:
        return "C+", 2.30
    elif marks >= 55:
        return "C", 2.00
    elif marks >= 50:
        return "C-", 1.70
    elif marks >= 45:
        return "D+", 1.30
    elif marks >= 40:
        return "D", 1.00
    else:
        return "F", 0.00


# ---------- File Handling ----------
def load_students():
    """Load student records from the data file into a list of dictionaries."""
    students = []
    if not os.path.exists(DATA_FILE):
        return students

    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            student_id, name, marks = parts[0], parts[1], float(parts[2])
            grade, point = calculate_grade(marks)
            students.append({
                "id": student_id,
                "name": name,
                "marks": marks,
                "grade": grade,
                "point": point
            })
    return students


def save_students(students):
    """Save the list of student dictionaries back to the data file."""
    with open(DATA_FILE, "w") as file:
        for s in students:
            file.write(f"{s['id']},{s['name']},{s['marks']}\n")


# ---------- Core Operations ----------
def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    for s in students:
        if s["id"] == student_id:
            print("A student with this ID already exists.\n")
            return

    name = input("Enter Student Name: ").strip()

    while True:
        try:
            marks = float(input("Enter Marks (0-100): ").strip())
            if 0 <= marks <= 100:
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    grade, point = calculate_grade(marks)
    students.append({
        "id": student_id,
        "name": name,
        "marks": marks,
        "grade": grade,
        "point": point
    })
    save_students(students)
    print(f"Student '{name}' added successfully with grade {grade}.\n")


def view_all_students(students):
    if not students:
        print("No student records found.\n")
        return

    print("\n" + "-" * 55)
    print(f"{'ID':<10}{'Name':<20}{'Marks':<8}{'Grade':<6}{'Point':<6}")
    print("-" * 55)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<20}{s['marks']:<8}{s['grade']:<6}{s['point']:<6}")
    print("-" * 55 + "\n")


def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()
    for s in students:
        if s["id"] == student_id:
            print("\nStudent Found:")
            print(f"ID    : {s['id']}")
            print(f"Name  : {s['name']}")
            print(f"Marks : {s['marks']}")
            print(f"Grade : {s['grade']} (Point: {s['point']})\n")
            return
    print("No student found with that ID.\n")


def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()
    for s in students:
        if s["id"] == student_id:
            print(f"Current Marks: {s['marks']}")
            while True:
                try:
                    new_marks = float(input("Enter new Marks (0-100): ").strip())
                    if 0 <= new_marks <= 100:
                        break
                    print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

            s["marks"] = new_marks
            s["grade"], s["point"] = calculate_grade(new_marks)
            save_students(students)
            print("Student record updated successfully.\n")
            return
    print("No student found with that ID.\n")


def delete_student(students):
    student_id = input("Enter Student ID to delete: ").strip()
    for s in students:
        if s["id"] == student_id:
            confirm = input(f"Are you sure you want to delete '{s['name']}'? (y/n): ").strip().lower()
            if confirm == "y":
                students.remove(s)
                save_students(students)
                print("Student record deleted.\n")
            else:
                print("Deletion cancelled.\n")
            return
    print("No student found with that ID.\n")


def sort_students_by_gpa(students):
    if not students:
        print("No student records found.\n")
        return

    sorted_list = sorted(students, key=lambda s: s["point"], reverse=True)
    print("\nStudents Ranked by Grade Point (Highest to Lowest):")
    print("-" * 55)
    print(f"{'Rank':<6}{'ID':<10}{'Name':<20}{'Grade':<6}{'Point':<6}")
    print("-" * 55)
    for i, s in enumerate(sorted_list, start=1):
        print(f"{i:<6}{s['id']:<10}{s['name']:<20}{s['grade']:<6}{s['point']:<6}")
    print("-" * 55 + "\n")


# ---------- Menu ----------
def print_menu():
    print("=" * 40)
    print("   GradeTrack - Student Result System")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Rank Students by GPA")
    print("7. Exit")
    print("=" * 40)


def main():
    os.makedirs("data", exist_ok=True)
    students = load_students()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            sort_students_by_gpa(students)
        elif choice == "7":
            print("Thank you for using GradeTrack. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()
