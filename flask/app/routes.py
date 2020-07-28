from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, AddUserForm
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
def index():
    all_posts = [
        {
            'title': 'Post 1',
            'subtitle': 'This is the content of post 1.'
        },
        {
            'title': 'Post 2',
            'subtitle': 'This is the content of post 2.'
        },
        {
            'title': 'Post 3',
            'subtitle': 'This is the content of post 3.'
        },
    ]
    return render_template('index.html', posts=all_posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin')
        return redirect(next_page)
    return render_template('login.html', form=form)
        

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    user = current_user.username
    posts = [
        {
            'title': 'Post 1',
            'subtitle': 'This is the content of post 1.'
        },
        {
            'title': 'Post 2',
            'subtitle': 'This is the content of post 2.'
        },
        {
            'title': 'Post 3',
            'subtitle': 'This is the content of post 3.'
        },
    ]
    return render_template('admin.html', posts=posts, user=user)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_login == datetime.utcnow()
        db.session.commit()


@app.route('/admin/new-user', methods=['GET', 'POST'])
@login_required
def newUser():
    form = AddUserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You've added a new user!")
    return render_template('new-user.html', form=form)
