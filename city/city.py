import requests
from flask import Flask, request

app = Flask(__name__)

city_zip = {
    "Acampo": "95220",
    "Acton": "93510",
    "Adelanto": "92301",
    "Adin": "96006",
    "Agoura Hills": "91301",
    "Aguanga": "92536",
    "Ahwahnee": "93601",
    "Alameda": "94501",
    "Alameda": "94502",
    "Alamo": "94507",
    "Albany": "94706",
    "Albion": "95410"
}

@app.route("/cityname/<string:city>", methods=["GET"])
def get_zip_from_city(city):
    if city in city_zip:
        zip_code = str(city_zip[city])
        weather_api_response = requests.get(f'http://second_serv:5001/weather/{zip_code}')
        weather = weather_api_response.text
        return f" The weather in {city} with zip: {zip_code} is {weather}"
    else:
        return "City not found"

if __name__ == "__main__":
    app.run()
