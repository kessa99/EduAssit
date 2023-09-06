from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))

@auth.route("/sign-up", methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userName = request.form.get('Username')
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email mst be greater than 3 characters.', category='error')
        elif len(userName) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
        elif len(name) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
        elif password1 is None or password2 is None:
            flash('Password fields are required.', category='error')
        elif password1 != password2:
            flash('password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must at least 7 characters', category='error')
        else:
            flash('Account created! Enjoy.', category='success')
    return render_template("signup.html")