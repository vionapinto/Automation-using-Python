import os
import cv2

images = os.listdir('images') # write file path inside'' i.e name of folder containing images

for image in images:
    print(image)
    # here it prints bear.jpeg
    # But in the next step it will look for bear.jpeg in the directory containing multiple_color_to_gray.py but it has to look one step inside images folder
    # So instead of imread('image',0) we need to write imread('images/bear.jpeg')

    gray = cv2.imread(f'images/{image}',0)
    print(gray)
    cv2.imwrite(f'grayimages/gray-{image}',gray)