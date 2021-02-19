import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('G:\python project\image processing\histogram\\fog.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.subplot(231), plt.imshow(gray, 'gray')
plt.subplot(234), plt.hist(img.ravel(), 256, [0, 255])   # .ravel()将图像变为一位数组

equalize = cv.equalizeHist(gray)
plt.subplot(232), plt.imshow(equalize, 'gray')
plt.subplot(235), plt.hist(equalize.ravel(), 256, [0, 255])

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_eql = clahe.apply(gray)
plt.subplot(233), plt.imshow(clahe_eql, 'gray')
plt.subplot(236), plt.hist(clahe_eql.ravel(), 256, [0, 255])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
