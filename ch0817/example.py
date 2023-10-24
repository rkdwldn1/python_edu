import time
from picamera import PiCamera

# 사진이 저장될 경로
photo_path = "/home/pi/webapps/"

# 사진 폴더 생성 (없는 경우에만)
try:
    os.makedirs(photo_path)
except FileExistsError:
    pass

# 카메라 객체 초기화
camera = PiCamera()

# 카메라 해상도 설정
camera.resolution = (1280, 720)  # 적절한 해상도 선택


# 사진 찍기
def take_photo():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    photo_filename = f"photo_{timestamp}.jpg"
    photo_fullpath = os.path.join(photo_path, photo_filename)
    camera.capture(photo_fullpath)
    print(f"Captured photo: {photo_filename}")


if __name__ == "__main__":
    take_photo()
