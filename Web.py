from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html.j2', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/remove_task', methods=['POST'])
def remove_task():
    task = request.form['task']
    if task in tasks:
        tasks.remove(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)