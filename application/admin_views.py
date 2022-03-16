from flask import render_template
from application import app

@app.route('/admin')
@app.route('/admin/')
def admin():
    return render_template('admin/admin.html')


@app.route('/admin/login')
@app.route('/admin/login/')
def admin_login():
    return render_template('admin/admin_login.html')