import cv2 as cv
import numpy as np

img = cv.imread('G:\python project\image processing\ROI\line.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
points = []
centers = []


def select_points(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:  # 左键点击，选择点
        cv.circle(img, (x, y), 10, (0, 0, 255), 2)
        points.append((x, y))
    if event == cv.EVENT_RBUTTONDOWN:  # 右键点击，选择点
        cv.circle(img, (x, y), 10, (0, 255, 0), 2)
        centers.append((x, y))


cv.imshow('image', img)
cv.setMouseCallback('image', select_points)

while 1:
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):  # 按'q'健退出循环
        break
cv.destroyAllWindows()

for i in points:
    for j in centers:
     cv.line(img, i, j, (0, 255, 0), thickness=3, lineType=8)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
