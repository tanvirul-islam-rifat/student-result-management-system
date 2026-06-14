# GradeTrack — Student Result Management System

A simple command-line application built in Python to manage student records — add, view, search, update, delete, and rank students by their grade point. Built as a course project for **CSE110 – Programming Language I** at BRAC University.

## Features

- **Add Student** — store ID, name, and marks
- **View All Students** — see all records in a formatted table
- **Search Student** — find a student instantly by ID
- **Update Marks** — edit a student's marks (grade is recalculated automatically)
- **Delete Student** — remove a record with confirmation
- **Rank by GPA** — sort and display students from highest to lowest grade point
- **Persistent Storage** — all data is saved to a text file using file handling, so records remain even after the program closes

## Grading Scale Used

| Marks Range | Grade | Grade Point |
|------------|-------|-------------|
| 90 - 100   | A+    | 4.00 |
| 85 - 89    | A     | 4.00 |
| 80 - 84    | A-    | 3.70 |
| 75 - 79    | B+    | 3.30 |
| 70 - 74    | B     | 3.00 |
| 65 - 69    | B-    | 2.70 |
| 60 - 64    | C+    | 2.30 |
| 55 - 59    | C     | 2.00 |
| 50 - 54    | C-    | 1.70 |
| 45 - 49    | D+    | 1.30 |
| 40 - 44    | D     | 1.00 |
| Below 40   | F     | 0.00 |

## How to Run

1. Make sure Python 3 is installed on your machine.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python3 gradetrack.py
```

5. Use the on-screen menu to interact with the system.

## Project Structure

```
student_result_management_system/
├── gradetrack.py      # Main program
├── data/
│   └── students.txt   # Stores student records (auto-created)
└── README.md
```

## Sample Run

```
========================================
   GradeTrack - Student Result System
========================================
1. Add Student
2. View All Students
3. Search Student by ID
4. Update Student Marks
5. Delete Student
6. Rank Students by GPA
7. Exit
========================================
Enter your choice (1-7): 1
Enter Student ID: 22101311
Enter Student Name: Tanvir
Enter Marks (0-100): 78
Student 'Tanvir' added successfully with grade B+.
```

## What I Learned

- Python fundamentals: variables, loops, conditionals, and functions
- Working with **lists of dictionaries** to manage structured data
- **File handling** (reading from and writing to text files) for persistent storage
- Building a clean, menu-driven CLI application
- Input validation and error handling using `try`/`except`

## Future Improvements

- Add support for multiple subjects and CGPA calculation
- Export records to CSV or JSON
- Add a simple GUI using Tkinter
