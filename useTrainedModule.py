import cv2
import time
import argparse

from ultralytics import YOLO
import supervision as sv


def drawResults(results, frame):
    # Vẽ bounding boxes và nhãn lên khung hình
    # for detection in results.pred:
    #     x, y, w, h = detection['box']
    #     label = detection['class']
    #     confidence = detection['conf'] # Độ tin cậy :)

    #     # Vẽ bounding box
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #     # Hiển thị nhãn và độ tin cậy
    #     text = f'{label} {confidence:.2f}'
    #     cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    for result in results:
    	xyxys = []
    	confidences = []
    	class_ids = []

    	boxes = result.boxes.cpu().numpy()
    	xyxys = boxes.xyxy
    	confidence = boxes.conf
    	for xyxy in xyxys:
    		# cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0,255,0), 1)
    		pass
    		

def parse_arguments() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="YOLOV8 live")
	parser.add_argument('--webcam-resolution', nargs=2, type=int, default=[1200, 720])
	args = parser.parse_args()
	return args

def main():
	args = parse_arguments()
	frame_width, frame_height = args.webcam_resolution

	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

	model = YOLO('best.pt') #đổi tên module ở đây

	#khởi tạo frame_count và mốc thgian
	frame_count = 0
	start_time = time.time()

	while True:
		ret, frame = cap.read() #đọc từng frame

		results = model(frame) #Kết quả

		#tính toán show FPS lên frame
		frame_count += 1
		elapsed_time = time.time() - start_time
		fps = frame_count / elapsed_time
		cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
		if elapsed_time >= 1:
			frame_count = 0
			start_time = time.time()

		#vẽ bounding boxes
		# drawResults(results, frame)

		#show frame lên màn hình (độ trễ 10ms)
		cv2.imshow('frame', results[0].plot())
		if (cv2.waitKey(10) == ord('q')):
			cv2.destroyAllWindows()
			break

if __name__ == '__main__':
	main()