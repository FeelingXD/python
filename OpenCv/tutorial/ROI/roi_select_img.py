import cv2 as cv , numpy as np

img = cv.imread('../../img/Lenna.png')

x,y,w,h = cv.selectROI('img',img,False)
if w and h:
    roi = img[y:y+h,x:x+w]
    cv.imshow('cropped',roi)
    cv.movewind('cropped',0,0)
    cv.imwrite('../../img/cropped2.png',roi)

cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()
