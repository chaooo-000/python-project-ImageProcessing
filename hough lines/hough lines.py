import cv2 as cv
import numpy as np

img = cv.imread('G:\python project\image processing\hough lines\\bg_fin.jpg', 1)
blur = cv.GaussianBlur(img, (3, 3), 0)  # 高斯模糊，矩阵长宽取3，标准差0
gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)  # 转换为灰度图
canny = cv.Canny(gray, 50, 150)

# lines = cv.HoughLines(canny, 1, np.pi / 180, 180)   # 像素分辨率1，弧度分辨率1，阈值180，返回三维数组
# for line in lines:
#     r, theta = line[0][0], line[0][1]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * r
#     y0 = b * r
#     x1 = int(x0 + 600 * (-b))  # a,b,x0,y0得出的是垂线那一点，要算出另外两个点才能画一条直线
#     y1 = int(y0 + 600 * a)
#     x2 = int(x0 - 600 * (-b))  # 600保证线能够画过整个图形
#     y2 = int(y0 - 600 * a)
#     cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)    # 宽度2

lines = cv.HoughLinesP(canny, 1, np.pi / 180, 20, minLineLength=5, maxLineGap=4)
res_line=[]
for line in lines:  # 对每一根线执行一次
    for x1, y1, x2, y2 in line:
        if abs(y2-y1) <= 1 and abs(x2-x1) >= 20:
            res_line.append((x1, y1, x2, y2))
            cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)    # 宽度2

cv.imshow("canny", canny)
cv.imshow("line", img)
cv.waitKey(0)
cv.destroyAllWindows()
