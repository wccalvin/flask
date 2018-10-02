from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    my_list = range(5)
    context = {'my_list': my_list}
    return render_template('layout.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
