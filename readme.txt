Sử dụng YOLO v8 để train HCN =)) và sử dụng: cần 3 file
	datacollection.py
		- Tác dụng: collect imgs để train, sử dụng pyautogui.screenshot() và cắt ghép, đánh số bla bla -> cho vào folder riêng
	
	trainModule.py
		- Yêu cầu 4 mục dưới (must have)
	test.yaml
		- Tác dụng: muốn train phải có file này
			- để ctrinh biết có bao nhiêu class
			- lưu đường dẫn tới folder dataset
	dataset(folder)
		- Tree directory:
			- dataset
				- images (chứa ảnh)
					- train  (90% ảnh)
					- val    (10% còn lại)
				- labels (chứa labels đã đánh dấu từ makesense.ai, số ảnh = số label)
					- train  (90% label)
					- val	 (10% còn lại)
	
	useTrainedModule.py
		- Tác dụng: như tên
		- module khi train xong tên là best.pt ở trong folder run, lấy ra mà quẩy
		- muốn train tiếp thì lấy last.pt ra train