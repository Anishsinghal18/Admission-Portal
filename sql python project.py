
import sqlite3

# Connect to the database
conn = sqlite3.connect('college_admission.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        course TEXT NOT NULL,
        admission_status TEXT DEFAULT 'Pending'
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        availability TEXT NOT NULL
    )
''')

# Function to add student data
def add_student(name, email, course):
    cursor.execute('INSERT INTO students (name, email, course) VALUES (?, ?, ?)',
                   (name, email, course))
    conn.commit()
    print("Student added successfully!")

# Function to delete student data
def delete_student(id):
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    print("Student deleted successfully!")

# Function to modify student data
def modify_student(id, name=None, email=None, course=None):
    if name:
        cursor.execute('UPDATE students SET name = ? WHERE id = ?', (name, id))
    if email:
        cursor.execute('UPDATE students SET email = ? WHERE id = ?', (email, id))
    if course:
        cursor.execute('UPDATE students SET course = ? WHERE id = ?', (course, id))
    conn.commit()
    print("Student data modified successfully!")

# Function to display student data
def show_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Course: {row[3]}, Admission Status: {row[4]}")

# Function to display course availability
def show_courses():
    cursor.execute('SELECT * FROM courses')
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Course Name: {row[1]}, Availability: {row[2]}")

# Function to update admission status
def update_admission_status(id, status):
    cursor.execute('UPDATE students SET admission_status = ? WHERE id = ?', (status, id))
    conn.commit()
    print("Admission status updated successfully!")

# Main program
while True:
    print("\nCollege Admission Portal")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Modify Student")
    print("4. Show Students")
    print("5. Show Courses")
    print("6. Update Admission Status")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        course = input("Enter course name: ")
        add_student(name, email, course)
    elif choice == '2':
        id = int(input("Enter student ID: "))
        delete_student(id)
    elif choice == '3':
        id = int(input("Enter student ID: "))
        name = input("Enter new name (optional): ")
        email = input("Enter new email (optional): ")
        course = input("Enter new course (optional): ")
        modify_student(id, name, email, course)
    elif choice == '4':
        show_students()
    elif choice == '5':
        show_courses()
    elif choice == '6':
        id = int(input("Enter student ID: "))
        status = input("Enter new admission status: ")
        update_admission_status(id, status)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the connection
conn.close()
