from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello flask. Looks like you don't have any name"

@app.route('/about-us')
def about():
    return '<b>About us page</b>'

@app.route('/username/<string:username>')
def name(username):
    return f"<h1>hello {username}</h1>"

if __name__ == "__main__":
    app.run(debug=True)