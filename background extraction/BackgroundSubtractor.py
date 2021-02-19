import cv2 as cv
import numpy as np

video = cv.VideoCapture('G:\python project\\video.mp4')  # 参数0表示摄像头
mog = cv.createBackgroundSubtractorMOG2(detectShadows=True)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
all_bg = []
c = 1  # 用于计时

while True:
    ret, img = video.read()
    if ret is True:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        fg = mog.apply(gray)  # 混合高斯模型
        ret, binary = cv.threshold(fg, 220, 255, cv.THRESH_BINARY)
        binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
        bg = mog.getBackgroundImage()

        if c % 50 == 0:  # 每隔50帧进行存储操作
            if len(all_bg) == 20:   # 每次对20张图进行处理
                del all_bg[0]
            all_bg.append(bg)
        c = c + 1

        cv.imshow('bg', bg)
        cv.imshow('thresh', binary)
        if cv.waitKey(1) & 0xFF == ord('q'):  # 按'q'健退出循环
            break
    else:
        break
video.release()  # 结束捕获

bg_fin = np.median(all_bg, axis=0)
cv.imwrite('G:\python project\\background extraction\\bg.jpg', bg)
cv.imwrite('G:\python project\\background extraction\\bg_fin.jpg', bg_fin)

cv.destroyAllWindows()
