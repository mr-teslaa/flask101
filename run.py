from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/username/<name>')
def username(name):
    return render_template('home.html', username=name)

if __name__ == "__main__":
    app.run(debug=True)