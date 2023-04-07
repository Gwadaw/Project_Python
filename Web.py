from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
# Les petites solutions de Lub1, ou comment cheese
def hello(name="World"):
    return render_template('hello.html.j2', name=name)