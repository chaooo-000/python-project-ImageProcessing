import cv2 as cv

img = cv.imread('G:\python project\OTSU threshold\line.jpg')
roi = cv.selectROI("roi", img, showCrosshair=True, fromCenter=False)
imgCrop = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
gray = cv.cvtColor(imgCrop, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
cv.imshow("binary", binary)
cv.waitKey(0)
cv.destroyAllWindows()
