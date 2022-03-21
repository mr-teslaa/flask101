from flask import Flask 

app = Flask(__name__)
app.config['SECRET_KEY'] = "hard to guess"

from application import views
from application import admin_views
