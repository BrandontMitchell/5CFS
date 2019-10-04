from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
import os, sys


proj_dir = os.path.dirname(os.path.abspath(__file__))
db_file = ""

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)