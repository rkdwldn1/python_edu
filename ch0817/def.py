"""
def mydef01():
    print("함수를 선언합니다.")


def mydef02(str="인수함수를 선언합니다."):
    print(str)


mydef01
mydef02
mydef02("인수를 넣습니다.")



# 여러 개의 인수를 입력 받아서 계산하는 함수 예제
def mydef01():
    i = 10
    j = 20
    print(i + j)


def mydef02(i, j):
    print(i + j)


def mydef03(i, j, p):
    if p == "+":
        print(i + j)
    elif p == "-":
        print(i - j)
    elif p == "*":
        print(i * j)
    elif p == "/":
        print(i / j)


mydef01()
mydef02(10, 20)

n = int(input("첫 번째 숫자를 입력합니다."))
m = int(input("두 번째 숫자를 입력합니다."))
p = input("연산자를 입력하세요")
mydef03(n, m, p)


#함수로 피라미드 만들기
def draw_pyramid(num_lines):
    for j in range(1, num_lines + 1):
        for i in range(num_lines - j):
            print(" ", end="")

        for i in range(j * 2 - 1):
            print("*", end="")

        print()


draw_pyramid(2)
draw_pyramid(4)
draw_pyramid(10)



# 피보나치 함수
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


print(fib(20))


fruits = []
fruits.append("알고리즘")
fruits.append("딥러닝")
fruits.append("데이터 웨어하우스")
fruits.append("가상화")
fruits.append("스토리지")


f = open("fruit.txt", "w")
for fruit in fruits:
    f.write(fruit)
    f.write("\n")

f.close()

f = open("fruit.txt", "r")
fruits = f.readlines()
f.close()

r_fruits = []
for f in fruits:
    r_fruits.append(f.strip())

print(r_fruits)
"""


# 평균을 result.txt에 복사
f = open("sample1.txt")
lines = f.readlines()
f.close()

print(lines)

r_lines = []
for i in lines:
    r_lines.append(i.strip())


print(r_lines)


sum = 0
for i in r_lines:
    sum += int(i)

average = sum / len(r_lines)
print(sum)

f = open("result.txt", "w")
f.write(str(average))
f.close

print(lines)


try:
    f = open("sample1.txt")
    lines = f.readlines()
except FileNotFoundError:
    print("파일이 없습니다. 파일명을 확인하세요")
finally:
    f.close()
