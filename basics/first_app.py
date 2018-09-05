#!usr/local/bin/python3

"""learning the basics of flask"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Clayton's macbook"

app.run(debug=True)