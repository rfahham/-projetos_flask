from flask import render_template
from flask import Flask
from app import app
app = Flask(__name__)

@app.route("/index")
@app.route("/")

def index():
    return render_template('templates/index.html')