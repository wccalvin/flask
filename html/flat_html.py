from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='world'):
    return """
<!doctype html>
<html>
    <head>
        <title>Flat HTML</title>
    </head>
    <body>
        <h1>Hello {}</h1>
    </body>
</html>
    """.format(name)


app.run(debug=True)
