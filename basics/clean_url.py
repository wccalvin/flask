"""learning the basics of flask"""

from __future__ import division
from flask import Flask


app = Flask(__name__)


# adding multiple routes
@app.route('/')
@app.route('/<name>')
def index(name="world"):
    return "Hello, {}.".format(name)


# add another route for accepting multiple params
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1+num2)


@app.route('/subtract/<int:num1>/<int:num2>')
@app.route('/subtract/<float:num1>/<float:num2>')
@app.route('/subtract/<float:num1>/<int:num2>')
@app.route('/subtract/<int:num1>/<float:num2>')
def subtract(num1, num2):
    return '{} - {} = {}'.format(num1, num2, num1-num2)


@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
def multiply(num1, num2):
    return '{} * {} = {}'.format(num1, num2, num1*num2)


@app.route('/divide/<int:num1>/<int:num2>')
@app.route('/divide/<float:num1>/<float:num2>')
@app.route('/divide/<float:num1>/<int:num2>')
@app.route('/divide/<int:num1>/<float:num2>')
def divide(num1, num2):
    try:
        solution = num1 / num2
    except ZeroDivisionError as why:
        return '{} / {} = {}'.format(num1, num2, why) + ' is illegal.'
    return '{} / {} = {}'.format(num1, num2, solution)

app.run(debug=True)

# use query string to say hello to multiple people '/?name=clayton'
