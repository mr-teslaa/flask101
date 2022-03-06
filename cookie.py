from urllib import response
from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/username/<name>')
def username(name):
    response =  make_response('<h2>We are using cookie. Are you agree?</h2>')
    response.set_cookie('Username', name)
    return render_template('home.html', username=name)

if __name__ == "__main__":
    app.run(debug=True)