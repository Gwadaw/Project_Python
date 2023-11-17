import sqlite3
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

conn = sqlite3.connect('todo.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        done INTEGER DEFAULT 0
    )
""")

conn.commit()
conn.close()

tasks = []

@app.route('/')
def tasks_list():
    return render_template('list.html.j2', tasks=tasks)

@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if content:
        tasks.append({'content': content, 'done': False})
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (content, done) VALUES (?, ?)", (content, False))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        conn.close()
    return redirect('/')

@app.route('/done/<int:task_id>', methods=['GET', 'POST'])
def resolve_task(task_id):
    if task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET done=? WHERE id=?", (tasks[task_id]['done'], task_id))
        conn.commit()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
