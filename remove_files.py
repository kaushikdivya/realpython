import os
mypath = "C:/Users/dk070h/Downloads/book1-exercises-master/chp09/practice_files/little pics"
for current, sub, image in os.walk(mypath):
	for img in image:
		img_path = os.path.join(current, img)
		if img.lower().endswith("jpg"):
			size = os.path.getsize(img_path)
			if size < 2000:
				print ("image size is less than 2000 byte - ", img_path)
				os.remove(img_path)
			else:
				print ("file size is greater then 2000 byte - ", img_path)
		else:
			print ("image is not jpg -", img_path)