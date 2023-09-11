from flask import Blueprint, render_template, request, flash, redirect, url_for
from .model import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login/', strict_slashes=False, methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('Username')
        password1 = request.form.get('password1')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password1):
                flash("logged in!")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("password is incorrect.", category='error')
        else:
            flash("Email does not exist.", category='error')
    return render_template("login.html", user=current_user)


@auth.route('/sign-up/', strict_slashes=False, methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is Already exists please change.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')

        elif password1 is None or password2 is None:
            flash('Password fields are required.', category='error')
        elif password1 != password2:
            flash('password don\'t match', category='error')
        elif len(password1) < 5:
            flash('Password must at least 5 characters', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember="True")
            flash('Account created! Enjoy.', category='success')
            return redirect(url_for('auth.login'))
    return render_template("signup.html", user=current_user)


@auth.route('/logout/', strict_slashes=False)
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))