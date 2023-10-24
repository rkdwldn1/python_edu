"""
user_input = "65, 45, 2, 3, 45, 8"

a = user_input.split(",")


sum = 0
for b in a:
    sum += int(b)

print(sum)


aa = [0, 0, 0, 0]
hap = 0
aa[0] = int(input("1번째 숫자:"))  # 숫자를 입력받아 a에 값을 대입(input 입력)
aa[1] = int(input("2번째 숫자:"))
aa[2] = int(input("3번째 숫자:"))
aa[3] = int(input("4번째 숫자:"))

hap = aa[0] + aa[1] + aa[2] + aa[3]
print(hap)

my_list = ["Python", "Beyoun", "hello", "compilers", "apple", "Apple"]
my_list.sort()
print(my_list)



#소수일때 myDict에 저장
def isOdd1(arg):
    return arg % 2 == 1


def isOdd2(arg):
    for i in range(2, arg):  # i가 2부터 arg까지
        if arg % i == 0:  # arg를 i로 나눴을 때 나머지가 0이면
            return False  # False
    return True


myDict = {x: x * x for x in range(2, 100) if isOdd2(x)}  # if문 함수가 True일때 myDict에 저장

print(myDict)


#시간 읽어와서 파일명 저장하기
import time
fruits = []
fruits.append("Strawberry")

filename = time.strftime("%Y%m%d_%H%M%S")
print(filename)

f = open(filename + ".txt", "w")
for fruit in fruits:
    f.write(fruit)
    f.write("\n")

f.close()
"""
