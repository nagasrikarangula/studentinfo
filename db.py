import sqlite3
def init_db():
    conn = sqlite3.connect('students.db')  # Ensure this matches your database configuration
    c = conn.cursor()
    # Create table
    c.execute('''
      CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        course TEXT,
        department TEXT,
        status TEXT,
        year INTEGER,
        grade TEXT
    )
    ''')
    conn.commit()
    conn.close()
if __name__ == '__main__':
    init_db()

