import requests
from flask import Flask, request
from flask import render_template  # render_template는 템플릿 폴더를 접근하여 HTML파일을 열어주는 작업을 한다.
from morse import *
from bs4 import BeautifulSoup


@app.route('/')  # 기본 경로
def home():  # home 함수 호출
    return render_template("index.html")


# render_template : flask 서버 내의 html문서를 반환해주는 메서드
# 반환을 해주면 템플릿 폴더에 있는 index.html를 플라스크가 열어준다


# GET:URL에 데이터를 붙여서 보내는 방식, POST:Body에 데이터를 넣어서 보내는 방식
@app.route("/morse_decoding", methods=["POST", "GET"])  # 디코딩한 정보을 서버에 보내주고 돌려받기 위한 내용
def morse_decoding():  # 함수 실행
    if request.method == "POST":  # 메서드 get
        inputMorse = request.form.get("inputMorse")  # 사용자로부터 입력을 받음

        Morse = (
            MorseCodeTranslator()
        )  # Morse라는 객체를 생성하고 morse.py에 있는 MorseCodeTranslator()클래스를 호출함

        change_text = set(inputMorse)  # 입력받은 inputMorse의 중복을 제거하여 change_text에 저장

        # 모스부호인지 체크
        if change_text.issubset(
            [" ", ".", "-"]
        ):  # 입력받은 데이터의 중복을 제거한 change_text의 값이 [" ", ".", "-"]과 일치한다면
            resulttext = Morse.morse_to_eng(
                inputMorse
            )  # resulttext는 morse.py에 있는 morse_to_eng()함수를 실행함

        # 알파벳 체크
        elif inputMorse.isalpha():  # 입력받은 데이터가 알파벳이라면
            resulttext = Morse.eng_to_morse(
                inputMorse
            )  # resulttext는 morse.py에 있는 eng_to_morse()함수를 실행

        # else 오류 출력
        else:
            resulttext = "error"  # 둘다 아니라면 error 메세지 출력

    return render_template(
        "index.html", result=resulttext
    )  # render_template 함수를 이용해서 index.html을 열어주고 index.html의 result에 resulttext값을 저장


if __name__ == "__main__":  # 실행
    app.run(host="0.0.0.0", port=5200)
