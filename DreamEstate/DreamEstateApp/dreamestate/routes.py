from dreamestate import app
from flask import render_template


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='Home Page')


@app.route('/about')
def about():
    return render_template('About.html',title='About')

@app.route('/account')
def account():
    return render_template('Account.html',title='Account')

@app.route('/register')
def register():
    return render_template('Register.html',title='Sign Up')


@app.route('/login')
def login():
    return render_template('Login.html',title='Login')
