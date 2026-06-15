# GradeTrack — Student Result Management System

A simple command-line application built in Python to manage student records — add, view, search, update, delete, and rank students by their grade point.

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
| 97 - 100   | A+    | 4.00 |
| 90 - 96    | A     | 4.00 |
| 85 - 89    | A-    | 3.70 |
| 80 - 84    | B+    | 3.30 |
| 75 - 79    | B     | 3.00 |
| 70 - 74    | B-    | 2.70 |
| 65 - 69    | C+    | 2.30 |
| 60 - 64    | C     | 2.00 |
| 57 - 59    | C-    | 1.70 |
| 55 - 56    | D+    | 1.30 |
| 52 - 54    | D     | 1.00 |
| 50 - 51    | D-    | 0.7  |
| Below 50   | F     | 0.00 |

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

## Technical Architecture

* **Language:** Python 3.x
* **Paradigm:** Procedural Programming & Modular Design
* **Data Storage:** Flat-file text database (`.txt`) with dynamic loading/saving
* **Interface:** Command Line Interface (CLI)

## Core Engineering Practices Demonstrated

* **CRUD Operations:** Full implementation of Create, Read, Update, and Delete lifecycles for managing persistent records.
* **In-Memory Data Management:** Efficiently handling and mutating lists of dictionaries in memory before committing state changes to disk.
* **Defensive Programming:** Strict input validation and exception handling (`try/except`) to prevent runtime crashes from invalid user inputs.
* **State Persistence:** Robust file I/O operations ensuring zero data loss between application sessions.

## Author

**Md. Tanvirul Islam Rifat**
* **GitHub:** [@tanvirul-islam-rifat](https://github.com/tanvirul-islam-rifat)
* **LinkedIn:** [Tanvirul Islam Rifat](https://www.linkedin.com/in/tanvirul-islam-rifat)
