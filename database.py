import sqlite3

def get_connection():
    conn = sqlite3.connect('attendance.db')
    return conn

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_no INTEGER UNIQUE NOT NULL,
        face_encoding BLOB NOT NULL
    )''')
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )''')
    
    conn.commit()
    conn.close()