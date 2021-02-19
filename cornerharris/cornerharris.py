import cv2 as cv
import numpy as np

img = cv.imread('G:\python project\contour\\arrow.jpg')
rows, cols, channels = img.shape
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
harris = cv.cornerHarris(gray, 2, 3, 0.04)
cv.imshow('harris', harris)

num = 0
for i in range(0, rows):
    for j in range(0, cols):
        if harris[i, j] > 0.01 * harris.max():
            img[i, j] = [0, 0, 255]
            num += 1
print(num)
cv.imshow('img2', img)

cv.waitKey(0)
cv.destroyAllWindows()
