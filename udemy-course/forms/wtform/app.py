from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


class InfoForm(FlaskForm):
    '''creating form'''

    name = StringField("What is your name?")
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = False

    form = InfoForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    context = {'form': form, 'name': name}
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
