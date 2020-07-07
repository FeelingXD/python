import cv2 as cv
import numpy as np

img= cv.imread('../../img/blankimg.png')

pts1 = np.array([[50,50],[150,150],[100,140],[200,240]], dtype=np.int32)
pts2 = np.array([[350,50],[250,200],[450,200]], dtype=np.int32)

#draw
cv.polylines(img,[pts1],False,(255,0,0))
cv.polylines(img,[pts2],False,(5,5,5),10)


cv.imshow('polyline',img)
cv.waitKey(0)
