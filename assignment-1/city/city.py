from flask import Flask, request

app = Flask(__name__)

city_zip = {
    "Acampo": 95220,
    "Acton": 93510,
    "Adelanto": 92301,
    "Adin": 96006,
    "Agoura Hills": 91301,
    "Aguanga": 92536,
    "Ahwahnee": 93601,
    "Alameda": 94501,
    "Alameda": 94502,
    "Alamo": 94507,
    "Albany": 94706,
    "Albion": 95410
}

@app.route("/zip_from_city", methods=["GET"])
def get_zip_from_city():
    city = request.args.get("city_name")
    if city:
        zip_code = city_zip.get(city, None)
        if zip_code:
            return {f"zip code for {city}": zip_code}
        else:
            return {"error": "City not found"}
    else:
        return {"error":"Please provide a city name"}

if __name__ == "__main__":
    app.run()
