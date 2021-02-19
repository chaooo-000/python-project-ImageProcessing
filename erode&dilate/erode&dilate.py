import cv2 as cv

img = cv.imread('G:\python project\erode&dilate\lena.jpg')

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

erode = cv.erode(img, kernel)
erode_2 = cv.erode(img, kernel, iterations=2)
dilate = cv.dilate(img, kernel)

mor_open = cv.morphologyEx(img, cv.MORPH_OPEN, kernel, iterations=2)
mor_close = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)


cv.imshow('erode_2', erode_2)
cv.imshow('mor_open', mor_open)


cv.waitKey(0)
cv.destroyAllWindows()
