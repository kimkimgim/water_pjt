import tflite_runtime.interpreter as tflite
import numpy as np

class WaterModel:
    def __init__(self, model_path="water_model.tflite"):
        self.interpreter = tflite.Interpreter(model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.height = self.input_details[0]['shape'][1]
        self.width  = self.input_details[0]['shape'][2]

    def preprocess(self, img):
        img = img.resize((self.width, self.height))
        arr = np.array(img, dtype=np.float32) / 255.0
        arr = np.expand_dims(arr, axis=0)
        return arr

    def infer(self, img):
        arr = self.preprocess(img)
        self.interpreter.set_tensor(self.input_details[0]['index'], arr)
        self.interpreter.invoke()

        output = self.interpreter.get_tensor(self.output_details[0]['index'])
        pred = int(np.argmax(output))  # 네 모델 형태에 따라 바꿀 수 있음
        return "물이 차오릅니다" if pred == 1 else "안전합니다."

        # 예외처리 코드 필요(알수없음의 경우)
