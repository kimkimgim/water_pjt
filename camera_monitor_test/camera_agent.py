import io         # 파일을 저장하지 않고 메모리에서 바로 처리할때
import time

from picamera2 import Picamera2


picam2 = Picamera2()

class CameraAgent():
    def__init__(self):              # 카메라 1회만 초기화 & 설정
        self.camera = Picamera2()
        self.camera_still_config = self.camera.create_still_configuration(
            main={
                'size': (1280, 768)
            }
        )
        self.camera.configure(self.camera_still_config)
        self.camera.start()
        time.sleep(2)

    def capture(self, is_bytearray=True):
        captured = self.camera.capture_image('main')

        # PIL 이미지 -> JPEG로 변형
        if is_bytearray:   
            result = io.BytesIO()
            captured.save(result, format='jpeg')

            return result.getvalue()

    return captured