# Extracting via python the resolution of the video i.e no. of pixels horizontally and vertically
# Extract total number of frames

import cv2

video = cv2.VideoCapture("video.mp4")

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
print(f'Width is: {width}')

height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f'Height is: {height}')

nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
print(f'No of frames: {nr_frames}')

fps = video.get(cv2.CAP_PROP_FPS)
print(f'Frames per second: {fps}')

print(width, height, nr_frames, fps)