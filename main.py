import requests
import urllib.parse

from flask import Flask, render_template, request
app = Flask(__name__)

API_KEY = ""

def get_forecast(location):

    coords = requests.get(f"https://nominatim.openstreetmap.org/search/{urllib.parse.quote(location)}?format=json").json() # gets lat / long for location... needed for API
    
    response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': coords[0]["lat"],
        'lng': coords[1]["lon"],
        'params': 'swellHeight'
    },
    headers={
        'Authorization': '' # API KEY GOES HERE!!!!
    }
    )
    return response


@app.route("/", methods=["POST", "GET"])
def root_page():
    if request.method == "POST":
        location = request.form["location"]
        data = get_forecast(location).json()
        return data
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run()