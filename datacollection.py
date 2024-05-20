import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

#nhận diện tay dùng HandDetector
#xuất ra 3 dạng: bth, crop, và crop(resize) trên nền trắng

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 15
imgSize = 300
couter = 0
labels = ['hello, thanks, yes']

while True:
	ret, frame = cap.read()
	# hands, img = detector.findHands(frame)
	# if hands:
	# 	hand = hands[0]
	# 	x, y, w, h = hand['bbox']

	# 	imgWhite = np.ones((imgSize,imgSize,3), np.uint8)*255

	# 	imgCrop = img[y-offset : y + h + offset, x-offset : x + w + offset]
	# 	imgCropShape = imgCrop.shape

	# 	aspectratio = h/w

	# 	if aspectratio > 1:
	# 		print(1)
	# 		k = imgSize / h
	# 		wCal = math.ceil(k*w)
	# 		imgResize = cv2.resize(imgCrop, (wCal, imgSize))
	# 		imgResizeShape = imgResize.shape
	# 		wGap = math.ceil((imgSize - wCal)/2)
	# 		imgWhite[:, wGap:wCal+wGap] = imgResize

	# 	else:
	# 		print(2)
	# 		k = imgSize / w
	# 		hCal = math.ceil(k*h)
	# 		imgResize = cv2.resize(imgCrop, (imgSize, hCal))
	# 		imgResizeShape = imgResize.shape
	# 		hGap = math.ceil((imgSize - hCal)/2)
	# 		imgWhite[hGap : hCal + hGap, :] = imgResize #đáp imgResize vô nền trắng

		# cv2.imshow('imgCrop', imgCrop)
		# cv2.imshow('imgWhite', imgWhite)

	cv2.imshow('frame', frame)
	key = cv2.waitKey(1)
	if key == ord('q'):
		cv2.destroyAllWindows()
		break
	if key == ord('s') :
		cv2.imwrite(f'imgs/img_{time.time()}.jpg', frame)