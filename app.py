from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)
def get_student_by_id(table_name, student_id):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM {table_name} WHERE id=?', (student_id,))
    student = c.fetchone()
    conn.close()
    return student
@app.route('/', methods=['GET', 'POST'])
def index():
    students = []
    if request.method == 'POST':
        student_id = request.form['student_id']
        student1 = get_student_by_id('student', student_id)  # To query 'student' table
        student2 = get_student_by_id('students', student_id)  # To query 'students' table
        if student1:
            students.append(student1)
        if student2:
            students.append(student2)
    return render_template('index.html', students=students)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

