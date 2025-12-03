from picamera2 import Picamera2
from PIL import Image
import time

def capture_image():
    picam = Picamera2()
    picam.start()
    time.sleep(2)
    frame = picam.capture_array()
    img = Image.fromarray(frame)
    return img
