import cv2

image = cv2.imread('galaxy.jpeg')
print(image.shape) # --> (779, 438, 3)

def calculate_size(scale_percentage, width, height):
    new_width = width * scale_percentage / 100
    new_height = height * scale_percentage / 100
    return(new_width, new_height)

print(calculate_size(10, image.shape[1], image.shape[0]))

def resize(image_path):
    pass