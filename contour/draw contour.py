import cv2 as cv
import numpy as np

img = cv.imread('G:\python project\contour\\arrow.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)  # 大津法
cv.imshow('binary', binary)
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(contours)
print(len(contours))
cv.drawContours(img, contours, -1, (0, 0, 255), 3)
cv.imshow('res', img)

# for contour in contours:
#     line = cv.fitLine(contour, cv.DIST_L1, 0, 0.01, 0.01)
#     k = line[1] / line[0]
#     x0, y0 = line[2], line[3]
#     x1 = int(x0 + 10)
#     y1 = int(y0 + 10*k)
#     x2 = int(x0 - 10)
#     y2 = int(y0 - 10*k)
#     cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.waitKey(0)
cv.destroyAllWindows()

