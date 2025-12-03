import os
import random
from PIL import Image

def load_image(path="./photo"):

    files = os.listdir(path)
    images = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    
    if not images:
            raise FileNotFoundError("photo 폴더에 이미지가 없어요!")
    
    selected = random.choice(images)
        
    full_path = os.path.join(path, selected)

    return Image.open(full_path)
