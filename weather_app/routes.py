from app import app
from flask import render_template, request, url_for, redirect, flash
from forms import SearchForm
import requests
import os
import json
from flask_googlemaps import Map, icons

@app.route('/',methods=['GET','POST'])
def index():
    searchForm = SearchForm()


    api_key = os.environ['WEATHER_API']
    maps_api = os.environ['MAPS_API']

    if searchForm.validate_on_submit():
        data = searchForm.zipcode.data
        req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={data}&appid={api_key}')
        weather_data = req.json()
        print(weather_data)
        weather_dict = {
            'city' : weather_data['name'],
            'temp' : '{:.2f}'.format((weather_data['main']['temp'] - 273.15) * (9/5) + 32)  ,
            'desc' : weather_data['weather'][0]['description'],
            'icon' : weather_data['weather'][0]['icon'],
            'coord' : weather_data['coord']
        }



        return render_template('index.html',form=searchForm,weather=weather_dict,maps_api=maps_api)
    return render_template('index.html', form=searchForm,weather='',maps_api=maps_api)


