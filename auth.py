from flask import Blueprint, render_template

auth = Blueprint('main', __name__)

@auth.route('/signup')
def signup():
    return 'Signup page'

@auth.route('/profile')
def login():
    return "Login users"

@auth.route()
def logout():
    return "Logout"