from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class ContactForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    message = TextAreaField('Message')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()

    if form.validate_on_submit():
        # Handle form submission (you can process the data as needed)
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # For now, just print the data to the console
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        # Optionally, you could save the data to a database or send an email

    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
