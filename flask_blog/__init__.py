from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '1f7f95379f823e09d87a6da0b35116d7'

# Set where SQLite DB is created => Root folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Instantiate SQLite DB
db = SQLAlchemy(app)

# Must do it here
from flask_blog import routes
