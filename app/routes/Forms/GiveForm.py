from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from app.routes.Classes import User
from flask import session
from app.routes.Classes import User

class GiveForm(FlaskForm):
    amount = IntegerField("Amount")
    recipient = SelectField(label="To", choices=[(row.name, row.name) for row in User.objects()])
    reason = StringField("Reason")
    category = SelectField(label="Category", choices = [('Helped others','Helped others'),('Did me a favor','Did me a favor'),('Did something for a teacher','Did something for a teacher'),('Class participation','Class participation'),('Community beautification','Community beautification')])
    submit = SubmitField("Submit")

    # Class method to ensure that each time you instantiate and new form the user names
    # are reloaded from the database.  You call it this way:
    # form = GiveForm.new()
    @classmethod
    def new(cls):
        # Instantiate the form
        form = cls()
        # Create a list of tuples from the DB
        recipientChoices = [(row.name, row.name) for row in User.objects()]
        # Sort the list
        recipientChoices.sort()
        # Update the choices for the recipient form field
        form.recipient.choices = recipientChoices
        return form
