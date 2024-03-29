from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:AMSroot@localhost:3306/Games"

db = SQLAlchemy(app)

from application import routes