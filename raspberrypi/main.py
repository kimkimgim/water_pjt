from detector import WaterModel
from mqtt import send_message
from save_photo import load_image

try:
    from camera_module import capture_image
    CAMERA_AVAILABLE = True
except:
    CAMERA_AVAILABLE = False

if __name__ == "__main__":
    model = WaterModel("water_model.tflite")

    # mode = "c"
    mode = "f"
    if not CAMERA_AVAILABLE:
            mode = "f"

    if mode == "c" and CAMERA_AVAILABLE:
        img = capture_image()
        result = model.infer(img)
        print(result)
        send_message(result)

    elif mode == "f":
        img = load_image()
        result = model.infer(img)
        print(result)
        send_message(result)

    else:
        print("잘못된 선택 또는 카메라 없음")
