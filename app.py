from flask import Flask, render_template, request, redirect, url_for, flash
from database import setup_database, get_connection
from register import register_face
from attendance import mark_attendance
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "attendance_secret_key"
setup_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        if not name or not roll:
            flash("Please enter all fields", "warning")
        else:
            register_face(name, roll)
            flash(f"{name} registered successfully!", "success")
            return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/attendance')
def attendance():
    mark_attendance()
    flash("Attendance process completed.", "success")
    return redirect(url_for('home'))

@app.route('/records')
def records():
    conn = get_connection()
    df = pd.read_sql_query("""
        SELECT s.name, s.roll_no, a.date, a.time
        FROM attendance a
        JOIN students s ON s.id = a.student_id
        ORDER BY a.date DESC, a.time DESC
    """, conn)
    conn.close()
    return render_template('records.html', tables=df.to_html(classes='table table-striped', index=False))

if __name__ == "__main__":
    app.run(debug=True)
