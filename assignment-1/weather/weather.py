from flask import Flask, request

app = Flask(__name__)

weather = {
    "95220": "Rainy",
    "93510": "cloudy",
    "92301": "windy",
    "96006": "snowy",
    "91301": "snowy",
    "92536": "rainy",
    "93601": "windy",
    "94501": "snowy",
    "94507": "rainy",
    "94706": "windy",
    "95410": "rainy"
}
  
@app.route('/weather/<string:zip_code>', methods=['GET'])
def weather_api(zip_code):
    if zip_code in weather:
        return weather[zip_code]
    else:
        return f"Weather information not available for {zip_code}"

if __name__ == "__main__":
    app.run(port=5001)
