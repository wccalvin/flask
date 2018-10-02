from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/puppy/<name>')
def pup_name(name):
    context = {'name': name}
    return render_template('puppy.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
