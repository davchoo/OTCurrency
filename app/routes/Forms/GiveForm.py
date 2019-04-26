from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from app.routes.Classes import User

"""
CSV VERSION
"""
# import pandas as pd
# import os
# def getNames():
#     cd = os.getcwd()
#     table = pd.read_csv(cd.replace('\\','/')+'/app/routes/Forms/data.csv')
#     student_names = table['Full Name'].unique()
#     data = list(zip(student_names, student_names))
#     return data

"""
DATABASE VERSION
"""
from flask import session
from app.routes.Classes import User

# full_name = session["displayName"]

class GiveForm(FlaskForm):
    amount = IntegerField("Amount")
    recipient = SelectField(label="To", choices=[(row.name, row.name) for row in User.objects()])
    reason = StringField("Reason")
    category = SelectField(label="Category", choices = [('Helped others','Helped others'),('Did me a favor','Did me a favor'),('Did something for a teacher','Did something for a teacher'),('Class participation','Class participation'),('Community beautification','Community beautification')])
    submit = SubmitField("Submit")

    @classmethod
    def new(cls):
        # Instantiate the form
        form = cls()
        recipientChoices = [(row.name, row.name) for row in User.objects()]
        recipientChoices.sort()
        # Update the choices for the agency field
        form.recipient.choices = recipientChoices
        return form
