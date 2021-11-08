from core import app, db
from core import login_manager
from flask import Flask, render_template, redirect, flash, url_for, request, session
from flask_login import login_user,logout_user,current_user, login_required

from core.user import user


@user.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    session.clear()
    flash('You are now logged out.', 'info')
    return redirect(url_for('main.index'))


@user.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
