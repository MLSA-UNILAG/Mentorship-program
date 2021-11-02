from core import app, db
from core import login_manager
from flask import Flask, render_template, redirect, flash, url_for, request, session
from core.forms import LoginForm, SignUpForm
from flask_login import login_user,logout_user,current_user, login_required
from core.models import User

from core.users import users


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and form.password.data == user.password:
            login_user(user)
            flash(f'Login successful! Welcome {user.username}','success')
            return redirect(url_for('main.index'))
        else:
            flash('Please check login details or signup to continue!','danger')
            return redirect(url_for('users.signup'))
    return render_template('login.html', form=form)


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('signup.html', title='Sign Up', form=form)


@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    session.clear()
    flash('You are now logged out.', 'info')
    return redirect(url_for('main.index'))


@users.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
