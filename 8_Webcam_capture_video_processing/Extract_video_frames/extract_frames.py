# Extracting frames and storing in images folder

import cv2

video = cv2.VideoCapture("video.mp4")
# we need 90 print statements!-- print(video.read())
# So we use a while loop instead

success, frame = video.read() # get first frame

count = 1
while success:
    cv2.imwrite(f'images/{count}.jpeg', frame) # write first frame in image file
    success, frame = video.read()  # thn get second frame
    count +=1