import cv2
from ultralytics import YOLO
from db import Food_data

model = YOLO("foodsnap-ai\weights\best.pt")

class yolo_model():
    def prediction(img):
        results = model.predict(img, conf = 0.6)
        classes = set(results[0].boxes.cls.tolist())
        class_ids = [int(cls) for cls in classes]

        foods = []
        for id in class_ids:
            food = Food_data.finder(id)

            if food:
                foods.append(food)