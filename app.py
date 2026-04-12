from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function (Helper)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# 1. Home Page Route
@app.route('/')
def index():
    conn = get_db_connection()
    tours = conn.execute('SELECT * FROM tours').fetchall()
    conn.close()
    return render_template('index.html', tours=tours)

# 2. Add Tour Route
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        budget = request.form['budget']

        conn = get_db_connection()
        conn.execute('INSERT INTO tours (title, description, budget) VALUES (?, ?, ?)',
                     (title, description, budget))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# 3. Delete Tour Route
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tours WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)