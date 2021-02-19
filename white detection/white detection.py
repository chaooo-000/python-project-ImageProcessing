import cv2 as cv
import numpy as np

lower_white = np.array([0, 0, 221])
upper_white = np.array([180, 30, 255])

img = cv.imread('G:\python project\white detection\\road.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # change to hsv model
mask_white = cv.inRange(hsv, lower_white, upper_white)   # get mask
cv.imshow('mask_white', mask_white)

res_white = cv.bitwise_and(img, img, mask=mask_white)   # detect white
cv.imshow('res_white', res_white)

img_copy = np.copy(img)
color_1 = [255, 0, 0]
img_copy[mask_white != 0] = color_1
cv.imshow('img_copy', img_copy)

cv.waitKey(0)
cv.destroyAllWindows()
