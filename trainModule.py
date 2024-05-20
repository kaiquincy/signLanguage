from ultralytics import YOLO

model = YOLO(task='detect')
results = model.train(data='hand_detect.yaml', epochs=30, device='cpu')

