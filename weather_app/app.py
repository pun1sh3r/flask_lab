from flask import Flask, render_template, url_for, redirect



app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"

import routes