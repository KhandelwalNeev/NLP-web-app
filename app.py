from flask import Flask, render_template, request, redirect
from db import database
import api

app = Flask(__name__)

dbo = database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('users_name')
    email = request.form.get('users_email')
    password = request.form.get('users_password')

    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html', message="Registration successful. Kindly login to proceed")
    else:
        return render_template('register.html', message='Email already exists')

        # return name + " " + email + ' ' + password


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search(email, password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect email/password')

    # return render_template("new.html",message = "You are logged in successfully")


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('ner.html')


@app.route('/perform_sentiment_analysis', methods=['post'])
def perform_sentiment_analysis():
    text = request.form.get('ner_text')
    response = api.sentiment_analysis(text)
    print(response)
    return 'something'


app.run(debug=True)