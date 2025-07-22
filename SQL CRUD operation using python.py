import sqlite3
# Connect to database (or create it)
conn = sqlite3.connect('student.db')
# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject1 TEXT NOT NULL,
                    Subject2 TEXT NOT NULL,
                    Mark1 INTEGER NOT NULL,
                    Mark2 INTEGER NOT NULL
                )''')

# Commit the changes
conn.commit()

# Insert multiple employee records
student = [
    (92301733016,'ASHUTOSH SINGH','PWP',"COA",95,80),
    (92301733017,'HARSH TRIVEDI','PWP',"COA",85,87),
    (92301733027,'VIRAJ VAGHASIYA','PWP',"COA",90,77),
    (92301733046,'SHIVAM BHATT', 'PWP',"COA",93,90),
    (92301733058,'DEVENDRASINH JADEJA','PWP',"COA",75,80)
]
# Using executemany to insert multiple records
cursor.executemany('''INSERT INTO student (Enrollment, name, subject1,subject2,Mark1,Mark2) 
                      VALUES (?, ?, ?, ?, ?, ?)''', student)

# Commit the changes
conn.commit()

# Fetch all student records
cursor.execute('SELECT * FROM student')
rows = cursor.fetchall()
# Display the results
print("All Student Records:")
for row in rows:
    print(row)

# Fetch student got more than 90
cursor.execute('SELECT name, subject2, mark2 FROM student WHERE Mark2 > 80')
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 80:")
for student in high_marks:
    print(student)

# Update MArk for Ashutosh kumar (COA)
cursor.execute('''UPDATE student SET Mark2 = 98 
                  WHERE name = 'ASHUTOSH SINGH' AND subject2 = 'COA' ''')

# Commit the changes
conn.commit()
# Verify the update
cursor.execute('SELECT name, MArk2 FROM student WHERE name = "ASHUTOSH SINGH"')
updated_mark = cursor.fetchone()
print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")

# Calculate the average Mark
cursor.execute('''SELECT AVG(Mark2) FROM student''')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students is: ${avg_mark:.2f}")

# Close the connection
conn.close()

