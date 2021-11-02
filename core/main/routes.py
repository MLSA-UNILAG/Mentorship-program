from flask import Flask, render_template, request
from app.main import main


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home Page')

@main.route('/about')
def about():
    return render_template('about.html')

