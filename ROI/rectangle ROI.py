import cv2 as cv

img = cv.imread('G:\python project\ROI\\bg_fin.jpg')
roi = cv.selectROI("roi", img, showCrosshair=True, fromCenter=False)
imgCrop = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
cv.imshow("imgCrop", imgCrop)
cv.imwrite('G:\python project\ROI\imgCrop.jpg', imgCrop)
cv.waitKey(0)
cv.destroyAllWindows()


