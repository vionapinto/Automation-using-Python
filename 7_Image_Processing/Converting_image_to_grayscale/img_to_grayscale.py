import cv2

#print(dir(cv2))

#color = cv2.imread('galaxy.jpeg',1) #1 means in color, 0 would be grayscale
#made up of 3 matrices of same dimension representing each pixel

#print(color)
#print(type(color))

color = cv2.imread('galaxy.jpeg',0) # Notice here we write 0 so that we get the img in gray-scale
cv2.imwrite('galaxy-gray.jpeg',color)

# now a gray scale image is created and saved.
