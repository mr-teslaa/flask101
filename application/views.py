from application import app
from flask import render_template
from application.forms import NameForm

@app.route('/')
def index():
    adesh = NameForm()
    return render_template('index.html', form=adesh)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500