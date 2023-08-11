
from flask import Flask
import requests
import os

app = Flask(__name__)
ow_api_key = os.environ["OPEN_WEATHER_API_KEY"]
ow_target_url = 'https://api.openweathermap.org/data/2.5/weather'

def get_request(lon, lat, fkey, skey):
    params={
        "lat":lat,
        "lon":lon,
        "appid":ow_api_key
    }

    res = requests.get(ow_target_url, params=params)
    return res.json()[fkey][skey]

@app.route("/temp/<float:lon>/<float:lat>")
def get_temperature(lon, lat):
    temp = round(float(get_request(lon, lat, "main", "temp")) - 273.15)
    return f"{temp} oCelsius"


@app.route("/humidity/<float:lon>/<float:lat>")
def get_humidity(lon, lat):
    humidity = get_request(lon, lat, "main", "humidity")
    return f"Humidity: {humidity}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)