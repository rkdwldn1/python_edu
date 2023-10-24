# 3,6,9게임 1~100까지 3,6,9일 경우 x로 출력 아닐경우 숫자 그대로 출력
for i in range(1, 100, 1):
    if (
        "3" in str(i) or "6" in str(i) or "9" in str(i)
    ):  # 3,6,9가 i리스트 안에 있다면 x를 출력 (찾을 문자 in 문자를 찾을 리스트)
        print("x", end=" ")
    else:
        print(i, end=" ")


# 키워드 인수
def repeat_print(message, count):
    for a in range(count):
        print(message)


repeat_print(count=3, message="안녕")
