from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    num_end = False
    user_name = request.args.get('user')
    lower_letter = any(i.islower() for i in user_name)
    upper_letter = any(i.isupper() for i in user_name)
    num_end = user_name[-1].isdigit()
    report_value = lower_letter and upper_letter and num_end
    context = {'lower': lower_letter, 'upper': upper_letter,
               'num_end': num_end, 'report': report_value}
    return render_template('report.html', **context)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
