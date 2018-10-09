from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret'


class SimpleForm(FlaskForm):

    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = SimpleForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        flash('Hello {}, Welcome!'.format(session['name']))

        return redirect(url_for('index'))

    context = {'form': form}

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
