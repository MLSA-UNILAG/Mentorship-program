from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from core import login_manager,db
from core.models import User,Post
from core.forms import LoginForm, SignUpForm, UpdateProfileForm


from core.main import main


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def index():
    posts = Post.query.all()
    return render_template('index.html', title='Home Page',posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.password.data == user.password:
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Login successful! Welcome {user.username}', 'success')
            # When the login view is redirected to, it will have a next variable in the query string,
            # which is the page that the user was trying to access.
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Please check login details or signup to continue!', 'danger')
            return redirect(url_for('main.signup'))
    return render_template('login.html', form=form)


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    gender=form.gender.data, date_of_birth=form.date_of_birth.data,
                    password=form.password.data, is_writer=form.is_writer.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! Proceed to login with the credentials you just provided.', 'success')
        return redirect(url_for('main.login'))
    return render_template('signup.html', title='Sign Up', form=form)

    
@main.route('/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('profile.html', title='Profile Page',user=user)


@main.route('/<username>/edit', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    form = UpdateProfileForm()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.gender.data = current_user.gender
        form.date_of_birth.data = current_user.date_of_birth
    elif form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.gender = form.gender.data
        current_user.date_of_birth = form.date_of_birth.data
        db.session.commit()
        flash('Account successfully updated!','success')
        return redirect(url_for('main.profile',username=current_user.username))
    return render_template('updateprofile.html',form=form)
