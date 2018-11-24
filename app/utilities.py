from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required
import datetime


class NameForm(FlaskForm):
    def __init__(self):
        self.name = StringField('What is your name ?', validators=[Required()])
        self.note = TextAreaField('Daily Note')
        self.submit = SubmitField('Submit')

class WorkLog_T():
    def __init__(self):
        self.date = '{:%Y-%m-%d}'.format(datetime.datetime.now())
        self.jira_tags = StringField('JIRA ID(s)')
        self.note = TextAreaField('Comment')
