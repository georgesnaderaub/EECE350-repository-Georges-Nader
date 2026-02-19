import sqlite3

# Connect to SQLite (in memory for testing)
conn = sqlite3.connect(':memory:')

# this is important because foreign keys are OFF by default in SQLite
conn.execute("PRAGMA foreign_keys = ON;")

cursor = conn.cursor()

# Helper function to inspect table contents
def print_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    print(f"\nTable: {table_name}")
    print(" | ".join(columns))
    print("-" * 30)

    for row in rows:
        print(" | ".join(str(value) for value in row))

# Create tables
cursor.execute("""
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT
)
""")

cursor.execute("""
CREATE TABLE registered_courses (
    student_id INT,
    course_id INT
)
""")

cursor.execute("""
CREATE TABLE grades (
    student_id INT,
    course_id INT,
    grade REAL CHECK (grade >= 0 AND grade <= 100)
)
""")

students = [
    (1, 'Alice', 20),
    (2, 'Bob', 22),
    (3, 'Charlie', 21)
]
cursor.executemany("INSERT INTO student VALUES (?, ?, ?)", students)

registered_course = [
    (1, 1),
    (2, 1),
    (3, 2),
    (1, 3),
    (2, 2)
]
cursor.executemany("INSERT INTO registered_courses VALUES (?, ?)", registered_course)

grade = [
    (1, 1, 20),
    (2, 1, 80),
    (3, 2, 100),
    (1, 1, 40),
    (2, 1, 20),
    (3, 2, 10),
    (1, 1, 90),
    (2, 1, 70),
    (3, 2, 0),
    (1, 3, 100),
    (1, 3, 10),
    (1, 3, 50),
    (2, 2, 10),
    (2, 2, 20),
    (2, 2, 30)
]
cursor.executemany("INSERT INTO grades VALUES (?, ?, ?)", grade)

conn.commit()

print_table(cursor, "student")
print_table(cursor, "registered_courses")
print_table(cursor, "grades")

print("Maximum grade per student:")
cursor.execute('''
SELECT student_id, course_id, MAX(grade)
  FROM grades
  GROUP BY student_id
  ORDER BY student_id''')
for row in cursor.fetchall():
    print(row)
print("\nAverage grade per student:")
cursor.execute('''
SELECT student_id, course_id, AVG(grade) FROM grades
GROUP BY student_id
''')
for row in cursor.fetchall():
    print(row)

conn.close()