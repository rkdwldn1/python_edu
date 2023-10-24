from flask import Flask, request  # flask 설정

app = Flask(__name__)


@app.route("/")  # 기본경로
def start():  # 경로 접속시 start 함수 실행
    return "Hello World"


# 라우팅 추가(동적 라우팅)
# 정적 라우팅과 달리 뷰함수의 매개변수로 받아서 실행


@app.route("/users/<username>")  # '/users/사용자명'
def user(username):  # 경로 접속시 user함수 실행, username을 매개변수로 받아옴
    return "반갑습니다 " + username + "님"


if __name__ == "__main__":
    app.run()  # 실행
