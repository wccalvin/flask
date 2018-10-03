from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup_form():
    return render_template('sign_up.html')


@app.route('/thankyou')
def thank_you():
    first_name = request.args.get('first')
    last_name = request.args.get('last')
    context = {'first': first_name, 'last': last_name}
    return render_template('thank_you.html', **context)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
