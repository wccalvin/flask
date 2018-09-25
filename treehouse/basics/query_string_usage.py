"""learning the basics of flask"""

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index(name="world"):
    name = request.args.get('name', name)
    return "Hello, {}.".format(name)


app.run(debug=True)

# use query string to say hello to multiple people '/?name=clayton'
