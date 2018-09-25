from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='world'):
    context = {'name': name}
    return render_template('index.html', **context)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    # return render_template('add.html', num1=num1, num2=num2)  # one way of doing it
    context = {'num1': num1, 'num2': num2}
    return render_template('add.html', **context)


app.run(debug=True)
