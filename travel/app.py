from flask import Flask, render_template, request
import csv
from urllib.parse import urlencode, unquote
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
myWeatherKey = os.environ.get("WEATHER_FORECAST_KEY")
app = Flask(__name__)

r_dict = {}

with open("C:/python/travel/city.csv", mode="r", encoding="UTF8") as inp: #csv사이트inp
    reader = csv.reader(inp)
    r_dict = {rows[0]: rows[1] for rows in reader}


def getWeather(city_id):
    url = "http://apis.data.go.kr/5050000/festivalStatusService"  # URL정보
    queryString = "?" + urlencode(
        {
            "ServiceKey": unquote(myWeatherKey),
            "pageNo": "1",
            "numOfRows": "10",
            "dataType": "JSON",
            "regId": city_id,  # 사용자가 입력했던 city_id
        }
    )

    response = requests.get(url + queryString)
    r_dict = json.loads(response.text)
    r_response = r_dict.get("response")
    r_body = r_response.get("body")
    r_item = r_body.get("items")

    item_list = r_item.get("item")

    for item in item_list:
        if item.get("totalCount") == 1:
            fst_name = item.get("FSTVL_NM")
            break

    return fst_name


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["name"]
        city_id = r_dict.get(city_name)
        print(city_id)

        if city_id is None:  # 입력받은 city_id 값이 없다면
            return render_template("index.html")  # 원래 화면으로 초기화

        fst_name = getWeather(city_name)

        # festival_info = festival_dict.get(city_name, None)
        # festival_name = None
        # festival_location = None
        # festival_phone = None

        # if festival_info:
        #     festival_name = festival_name["name"]
        #     festival_location = festival_location["location"]
        #     festival_phone = festival_phone["phone"]

        return render_template(
            "index.html",
            city_name=city_name,
            festival_name=city_id,
            festival_location=festival_location,
            festival_phone=festival_phone,
        )
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
