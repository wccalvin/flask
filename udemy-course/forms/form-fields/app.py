from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextField, TextAreaField,
                     SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


class InfoForm(FlaskForm):

    name = StringField('What is your name?', validators=[DataRequired()])
    engineer = BooleanField('Are you an Engineer?')
    qualification = RadioField('Please choose your qualification:',
                               choices=[('qual_one', 'MS'), ('qual_two', 'Phd')])
    computer_language = SelectField(
        u'Pick your favorite programming language:',
        choices=[('py', 'Python'), ('js', 'JavaScript'), ('java', 'Java')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['engineer'] = form.engineer.data
        session['qualification'] = form.qualification.data
        session['computer_language'] = form.computer_language.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thank_you'))

    context = {'form': form}
    return render_template('index.html', **context)


@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
