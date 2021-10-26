from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from models import User



app = Flask(__name__)
app.secret_key = 'secretkeyhardcoded'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'




import routes, models



