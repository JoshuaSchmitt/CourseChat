from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joshua'}
    return render_template('index.html', user = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    """
    form.validate_on_submit() will return false if a GET request is sent and 
    will continue onto the render_template statement. If a POST request is sent 
    it will run the validators and may return true.
    """
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',form = form )
