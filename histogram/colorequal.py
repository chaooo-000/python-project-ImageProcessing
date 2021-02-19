import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('G:\python project\histogram\direction.jpg')
b, g, r = cv.split(img)
eb = cv.equalizeHist(b)
eg = cv.equalizeHist(g)
er = cv.equalizeHist(r)
merged = cv.merge([eb, eg, er])
cv.imshow('img', img)
cv.imshow('res', merged)

cv.waitKey(0)
cv.destroyAllWindows()
