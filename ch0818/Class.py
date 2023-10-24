# self는 메서드를 호출하는 객체 self:자기자신
# 특수한 메서드 __init__ : 객체를 만들때 자동으로 호출, 생성자와 비슷함
class AutoMobile:
    def __init__(self, str):
        self.name = str  # str 초기화

    def velocityPlus(self):
        self.velocity = self.velocity + 10

    def velocityDown(self):
        self.velocity = self.velocity - 10

        if self.velocity < 0:
            self.velocity = 0

    def velocity(self):
        a = input("속도:")
        self.velocity = int(a)


ac = AutoMobile("푸조")  # ac 객체 생성, AutoMobile init호출
ac.velocity()
ac.velocityPlus()  # velocityPlus 함수 호출
print(ac.name + "의 속도는 %d입니다." % ac.velocity)
