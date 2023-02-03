from flask import Flask, request

app = Flask(__name__)

zip_codes = {
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
  
@app.route("/weather_from_zip", methods=["GET"])
def get_weather_from_zip():
    zip_code = request.args.get("zip_code")
    if zip_code:
        weather = zip_codes.get(str(zip_code), None)
        if weather:
            return {f"weather condition for zip({zip_code})": weather}
        else:
            return {"error": "Zip code not found"}
    else:
        return {"error": "Please provide a zip code"}

if __name__ == "__main__":
    app.run()
