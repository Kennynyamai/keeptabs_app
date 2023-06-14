from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Employee
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        employee = Employee.query.filter_by(email=email).first()
        if employee:
            if check_password_hash(employee.password, password):
                flash('logged in succesfully', category='success')
                login_user(employee, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstname = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        employee =  Employee.query.filter_by(email=email).first()
        if employee:
            flash('Email Already Exists', category='error')
        elif len(email) < 4:
            flash("Email must be geater than 3 characters.", category='error')
        elif len(firstname) < 2:
            flash("Email must be geater than 1 characters", category='error')
        elif password1 != password2:
            flash("Your passwords dont match", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category='error')
        else:
            new_employee = Employee(email=email, first_name=firstname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_employee)
            db.session.commit()
            login_user(new_employee, remember=True)
            flash("User created succesfully", category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)

@auth.route('/logout')
@login_required  
def logout():
    logout_user()
    return redirect(url_for('auth.login'))