from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .model import Community
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)



@views.route('/subject')
@login_required
def subject():
    return render_template('subject.html', user=current_user)



@views.route('/book')
def book():
    return render_template('books.html', user=current_user)



@views.route('/community', methods=['GET', 'POST'])
@login_required
def community():
    posts = Community.query.all()
    if request.method == "POST":
        text= request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Community(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created', category='success')
    return render_template('community.html', user=current_user, posts=posts)

@views.route('/delete-post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Community.query.get_or_404(post_id)
    if post.author == current_user:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', category='success')
    else:
        flash('You are not authorized to delete this post', category='error')
    return redirect(url_for('views.community'))




@views.route('/contact')
def contact():
    return render_template('contact.html')