from flask import Blueprint, render_template, request, session
from flask_login import  login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/location')
def location():
    return render_template('location.html')



@views.route('/submit-location', methods=['POST'])
def submit_location():
    location = request.form.get('location')
    # Process the location data as needed
    print(type(location))
    return 'Location submitted: ' + location

@views.route('/logged_in_users')
def logged_in_users():
    return f"{current_user.first_name}"
