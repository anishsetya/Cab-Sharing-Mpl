from flask import Blueprint, render_template, request,flash, redirect, url_for
from .models import User
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth= Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password1')
        print("password ", password)
        user = User.query.filter_by(email=email).first()
        if user:
            print(user.password,password)
            if (user.password== password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    # data=request.form
    # print(data)
    return render_template("login.html",bol=False)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods =['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 charecters', category='error')
        elif len(password1)<7:
            flash('Password must be greater than 7 charecters', category='error')
        elif (password1!=password2):
            flash('Passwords not matching', category='error')
        else:
            print(email,first_name,password1)
            new_user = User(email=email, name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created succesfully',category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")