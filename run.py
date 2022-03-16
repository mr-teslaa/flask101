from flask import Flask 
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



# @app.route('/hossainfoysal')
# def hfoysal():
#     return redirect('https://hossainfoysal.com')

if __name__ == "__main__":
    app.run(debug=True)