from flask import render_template, url_for, flash, redirect
from flask_blog import app
from flask_blog.models import User, Post
from flask_blog.forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'March 27, 2020'
    },
    {
        'author': 'Roenz Aberin',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'March 28, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    # name = request.args.get("name", "World")
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
