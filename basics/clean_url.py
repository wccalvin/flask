"""learning the basics of flask"""

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


app.run(debug=True)

# use query string to say hello to multiple people '/?name=clayton'
