
from flask import request, render_template, flash, redirect,url_for,Flask
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'secretkeyhardcoded'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


import models, routes