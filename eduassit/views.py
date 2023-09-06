from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/subject')
def subject():
    return render_template('subject.html')

@views.route('/book')
def book():
    return render_template('books.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')