from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# initialize Flask
app = Flask(__name__, static_folder='static') # Specify static folder

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'secret'

# initialize database
db = SQLAlchemy(app)

# import routes / avoid circular imports
from routes import *

if __name__ == '__main__':
    from models import Expense  # Import your models
    # Create tables inside the app context
    with app.app_context():
        db.create_all()
    app.run(debug=True)