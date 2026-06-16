import sqlite3

def add_student():
    name = input("Enter Student Name: ")

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name) VALUES(?)",
        (name,)
    )

    conn.commit()
    conn.close()

    print("Student Added Successfully!")


def view_students():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        print(student)

    conn.close()


def mark_attendance():
    student_id = int(input("Enter Student ID: "))
    date = input("Enter Date (YYYY-MM-DD): ")
    status = input("P for Present / A for Absent: ")

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance(student_id, date, status) VALUES (?, ?, ?)",
        (student_id, date, status)
    )

    conn.commit()
    conn.close()

    print("Attendance Marked Successfully!")


mark_attendance()