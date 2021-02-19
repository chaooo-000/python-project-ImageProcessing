import cv2 as cv
import numpy as np

img = cv.imread('G:\python project\ROI\line.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
points = []


def draw_roi(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:  # 左键点击，选择点
        cv.circle(img, (x, y), 10, (0, 0, 255), 2)
        points.append((x, y))


cv.imshow('image', img)
cv.setMouseCallback('image', draw_roi)

while 1:
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):  # 按'q'健退出循环
        break
cv.destroyAllWindows()

points = np.array(points, np.int32)
points = points.reshape((-1, 1, 2))
mask = cv.fillPoly(img_copy1, [points], (0, 0, 0))
cv.imshow("mask", mask)
ROI = cv.bitwise_xor(mask, img_copy2)
cv.imshow("ROI", ROI)
cv.waitKey(0)
cv.destroyAllWindows()
