from flask import Flask, render_template, url_for, redirect
from flask_googlemaps import GoogleMaps


app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"
GoogleMaps(app,key="AIzaSyB_NUMCjEzDQznT8QfLjiAfokCCXPDRTHI")
import routes