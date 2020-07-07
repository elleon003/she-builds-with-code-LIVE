from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}') 
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/admin')
def admin():
    return render_template('admin.html')
