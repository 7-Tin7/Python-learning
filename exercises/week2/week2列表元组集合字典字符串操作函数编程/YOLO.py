from ultralytics import YOLO
result = YOLO("yolov8n.pt").predict(source='0',show=True)