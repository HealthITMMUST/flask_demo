from flask import Flask
from flask import render_template
import requests
from werkzeug.wrappers import json

auth = {
    "user": "admin",
    "password": "district"
}

app= Flask(__name__)
@app.route('/')
def index():
    data_elements_url = "https://play.dhis2.org/2.34.6/api/dataElements"
    data_elements = get_json(data_elements_url, auth)['dataElements']

    print(data_elements)
    return render_template("home.html",data_elements=data_elements)


def get_json(url, auth):
    user = auth['user'];
    password = auth['password']

    r = requests.get(url, auth=(user, password))
    return r.json()

