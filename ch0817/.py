"""
print('주석 예제입니다.')

#숫자형 : 정수 및 실수를 표현하는 타입
a=123
print(type(a)) #type함수는 변수의 타입을 리턴
a=100*100
a,b=9,2
print(a*b)

#문자형 : 문자열을 표현하는 타입
a="파이썬 만세"
print(a)
print(type(a))
b='python go'
print(type(b))
print(b)

#문자형 : split.join 
a="a:b:c:d"
b=a.split(":")
print(b) #['a','b','c','d']
c="#".join(b)
print(c) #a#b#c#d

#전화번호, 주민등록번호를 split로 구분
phoneNumber="010-1234-4567"
a=phoneNumber.split("-")
print(a)

address="1234567-1234567"
b=address.split("-")
print(b)

#리스트를 사용하지 않고 숫자형 변수 4개를 선언하여 출력한 예
a,b,c,d=0,0,0,0 
hap=0
a=int(input("1번째 숫자:")) #숫자를 입력받아 a에 값을 대입(input 입력)
b=int(input("2번째 숫자:")) 
c=int(input("3번째 숫자:"))
d=int(input("4번째 숫자:"))
hap=a+b+c+d
print("합계=%d" %hap) #%d는 % 뒤에 선언한 hap값이 대입


#리스트 변수를 선언하여 앞 예제를 수정
aa=[0,0,0,0]
hap=0
aa[0]=int(input("1번째 숫자:")) #숫자를 입력받아 a에 값을 대입(input 입력)
aa[1]=int(input("2번째 숫자:")) 
aa[2]=int(input("3번째 숫자:"))
aa[3]=int(input("4번째 숫자:"))

hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계2=%d"%hap)


3
#가변 리스트 사용
aa=[]
aa.append(100)
aa.append(2)

#리스트 슬라이싱
aa=[10,20,30,40,50,60,70]
print("aa[-1]은 %d, aa[-2]는 %d"%(aa[-1],aa[-2]))
print(aa[1::2])
print(aa[:])
print(aa[:1])


my_list=[0,1,2,3,4,5]
print(id(my_list)) #주소값을 보는 함수 id

my_list[1:3]=["A","B","C"]
print(id(my_list))

print(my_list)

my_list=[0,1,2,3,4,5]
print(id(my_list)) #주소값을 보는 함수 id

my_list[1:5]=["A","B"]
print(id(my_list))

print(my_list)


aa=[30,10,20]
print("현재의 리스트:%s"%aa)
aa.append(40)
print("append 후의 리스트:%s"%aa)
aa.pop()
print("pop 후의 리스트:%s"%aa)
aa.sort()
print("sort 후의 리스트:%s"%aa)
aa.reverse()
print("reverse후의 리스트:%s"%aa)
aa.insert(2,222)
print("insert(2,222) 후의 리스트:%s"%aa)
print("20값의 위치:%d"%aa.index(20))
aa.remove(222)
print("remove(222) 후의 리스트:%s"%aa)
aa.extend([77,88,77])
print("extend([77,88,77]) 후의 리스트:%s"%aa)
print("77값의 개수:%d"%aa.count(77))



my_list = ["클라우드","인공지능","CLI","GUI","OUI","NUI","컨테이너","가상화","알고리즘","빅데이터","운영체제"]

my_list.reverse()
print(my_list)

a=[1,2,3]
print(id(a))

a=a+[4,5]
print(id(a))
print(a)

b=[1,2,3]
print(id(b))

b.extend([4,5])
print(id(b))
print(b)


aa=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(aa[0])
print(aa[0][0])
print(aa[1][2])


str = "파이썬 문자열"
print(str[0])
print(str[-1])

card = "red", 4, "python", True
print(card)
print(card[1])



card = "red", 4, "ptyhon", True
a, b, c, d = card
print(a)
print(b)
print(c)
d = False
print(d)


my_tuple = ("사과", "딸기", "복숭아")
print(my_tuple.index("복숭아"))


#집합(set)
S = {100, 55, 1, 1, 1, 1, 2, 3} #중복 제거
print(S)

K = {5, 6, 7}
K.add(1) #1이라는 값을 추가
print(K)


#집합(set)
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

print("합집합:", A | B)
print("교집합:", A & B)
print("차집합:", A - B)
print("대칭차집합:", A ^ B) #합집합-교집합



d = {}
d = dict()
d = {
    "바나나": "외떡잎식물 생각목 파초과 바나나속에 속하는 식물의 총칭",
    "아이언맨": "여심을 사로잡는 매력적인 미소의 백만장자 플레이보이 토니 스타크",
    123: 456,
}

d1 = {"one": 1, "two": 2, "three": 3}
d2 = dict({"three": 3, "one": 1, "two": 2})
d3 = dict({"one": 1, "three": 3}, two=2)
d4 = dict(one=1, two=2, three=3)

# 튜플의 리스트
d5 = dict([("two", 2), ("one", 1), ("three", 3)])

# zip의 기능을 추측
d6 = dict(zip(["one", "two", "three"], [1, 2, 3]))

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)


#딕셔너리 (KEY값과 VALUE값이 한 쌍으로 저장되는 타입)
d = {"캡틴": "Captain", "캡틴": "아메리카"}
print(d)

d = {"A": 65, "B": 66, "C": 67}
print(d["B"])


# 딕셔너리
d = {"번호": 10, "성명": "코난", "나이": 23, "사는곳": "서울"}
print(d)

print(type(d))

print(d["나이"])

d["나이"] = 24
print(d["나이"])

d["직업"] = "탐정"
print(d)

print(d.keys())
print(d.values())

print("사는곳" in d)
del d["사는곳"]
print("사는곳" in d)

print(d)


my_list = [1, 2, 3, 4, 5]
del my_list[0:6:2] #0번째, 2번째 4번째 list 삭제
print(my_list)


a = {"A": 90, "B": 80, "C": 65}
print(a["A"])
print(a["B"])

print(a["C"])
print(a.get("C"))


# 문제) A학생의 50점 이상 총합을 구하세요(while,A.pop()함수 사용)
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

sum = 0
while A:
    score = A.pop()
    if score >= 50:  # socre가 50이상이라면
        sum += score

print(sum)


user_input = "65, 45, 2, 3, 45, 8"
a = user_input.split(",")

for b in a:
    sum(b)

    print(b)


# 구구단 출력
user_input = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))

for i in range(1, 10, 1):
    print(user_input * i, end=" ")
"""
