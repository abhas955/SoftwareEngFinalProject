from sqlalchemy.sql.functions import current_user

from dreamestate import db
from dreamestate import app
from flask import render_template,redirect,url_for,flash
from dreamestate.forms import RegistrationForm,LoginForm
from dreamestate.models import User as User

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

@app.route('/register',methods=['POST','GET'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}',category='success')
        return redirect(url_for('login'))
    return render_template('Register.html',title='Sign Up',form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and form.password.data==user.password:

            flash(f'Logged in successfully for {form.email.data}',category='success')
            return redirect(url_for('account'))


        else:
            flash(f'Login unsuccessful for {form.email.data}',category='danger')


    return render_template('Login.html',title='Login',form=form)


