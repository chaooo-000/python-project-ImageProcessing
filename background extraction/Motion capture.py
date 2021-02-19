import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)  # 参数0表示摄像头
mog = cv.createBackgroundSubtractorMOG2(detectShadows=True)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

while True:
    ret, img = video.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    fg = mog.apply(gray)  # 混合高斯模型
    ret, binary = cv.threshold(fg, 220, 255, cv.THRESH_BINARY)
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)

    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓
    for c in contours:
        if cv.contourArea(c) > 500:
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    cv.imshow('detection', img)
    if cv.waitKey(1) & 0xFF == ord('q'):  # 按'q'健退出循环
        break
video.release()
cv.destroyAllWindows()
