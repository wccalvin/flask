from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to puppy latin app. Go to /puppy/[Your Puppy Name] to convert to puppy latin.</h1>'


@app.route('/puppy/<name>')
def puppy(name):
    if name.endswith('y'):
        latin_name = name[:-1] + 'iful'
        return '<h1>Hi {}! Your puppy-latin name is {}</h1>'.format(name, latin_name)
    else:
        latin_name = name + 'y'
        return '<h1>Hi {}! Your puppy-latin name is {}</h1>'.format(name, latin_name)


if __name__ == '__main__':
    app.run(debug=True)
