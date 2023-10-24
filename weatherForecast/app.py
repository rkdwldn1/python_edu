from flask import Flask, render_template, request
import requests  # pip install requests
from urllib.parse import urlencode, unquote
import json
import csv
from dotenv import load_dotenv
import os

load_dotenv()
myWeatherKey = os.environ.get(
    "FESTIVEL_FORECAST_KEY"
)  # .env 파일에서 환경 변수를 로드하여 myWeatherKey 변수에 저장합니다.
print(myWeatherKey)

app = Flask(__name__)  # 애플리케이션 초기화

# Config

city_dict = {}

with open(
    "C:/python/weatherForecast/city.csv", mode="r", encoding="UTF8"
) as inp:  # csv 경로 열기, as를 통해 inp라는 별칭으로 사용
    reader = csv.reader(
        inp
    )  # reader함수를 통해 inp라는 별칭으로 저장된 .csv파일을 불러온 후 reader라는 변수에 저장
    city_dict = {rows[0]: rows[1] for rows in reader}
    # city.csv 파일로부터 정보를 읽어와 city_dict 딕셔너리에 저장합니다.

print(city_dict)

 #city_id는 사용자가 선택한 도시
def getWeather(city_id): #사용자가 선택한 도시 정보를 가져와 온도와 날씨 값을 반환하는 함수
    url = "http://apis.data.go.kr/1360000/VilageFcstMsgService/getLandFcst"  # URL정보
    queryString = "?" + urlencode(
        {
            "ServiceKey": unquote(myWeatherKey),
            "pageNo": "1",
            "numOfRows": "10",
            "dataType": "JSON",
            "regId": city_id,  # 사용자가 입력했던 city_id
        }
    )

    response = requests.get(url + queryString) #api에 GET요청을 보내서 url의 날씨 정보를 가져온다.
    r_dict = json.loads(response.text) #API 응답으로 받은 JSON 형식의 텍스트 데이터를 파싱하여 딕셔너리 형태로 변환합니다.
    r_response = r_dict.get("response")#딕셔너리에서 "response" 키에 해당하는 값을 가져옵니다. 이 값은 API 응답 데이터 중 "response" 객체를 의미
    r_body = r_response.get("body")  #"response" 객체에서 "body" 키에 해당하는 값을 가져옵니다. 이 값은 실제 날씨 데이터가 포함된 "body" 객체를 의미합니다.
    r_item = r_body.get("items") #body" 객체에서 "items" 키에 해당하는 값을 가져옵니다. 이 값은 날씨 정보가 담겨있는 "items" 객체를 의미합니다.

    item_list = r_item.get("item") #body" 객체에서 "items" 키에 해당하는 값을 가져옵니다. 이 값은 날씨 정보가 담겨있는 "items" 객체를 의미합니다.

    for item in item_list:
        if item.get("numEf") == 1: #현재 순회 중인 아이템의 "numEf" 키에 해당하는 값이 1인지 확인합니다. 이 값은 예보의 시간대를 나타내며, 1은 현재 시간의 예보를 의미합니다.
            temp = item.get("ta") #현재 시간의 예보일 때, 해당 아이템의 "ta" 키에 해당하는 값을 가져와 temp 변수에 저장합니다. "ta"는 온도를 의미합니다.
            weather = item.get("wf") #현재 시간의 예보일 때, 해당 아이템의 "wf" 키에 해당하는 값을 가져와 weather 변수에 저장합니다. "wf"는 날씨 상태를 의미합니다.
            break

    return temp, weather #날씨와 온도 값을 반환 


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["name"]
        city_id = city_dict.get(city_name)
        print(city_id)

        if city_id == None:
            return render_template("index.html")

        temp, weather = getWeather(city_id)

        return render_template(
            "index.html",
            temp=temp,
            weather=weather,
            city_name=city_name,
        )
    else:
        return render_template("index.html")  # 사용자가 입력하기 전에는 index.html창이 열림


if __name__ == "__main__":
    app.run(debug=True)
