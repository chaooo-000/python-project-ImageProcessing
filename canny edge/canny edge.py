import cv2 as cv

img = cv.imread('G:\python project\image processing\canny edge\lena.jpg')
blur = cv.GaussianBlur(img, (3, 3), 0)  # 高斯模糊，长宽取3，标准差0
gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)  # 转换为灰度图
canny = cv.Canny(gray, 50, 150)

cv.imshow("img", img)
cv.imshow("Canny Edge", canny)
cv.waitKey(0)
cv.destroyAllWindows()
