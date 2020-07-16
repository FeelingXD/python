# roi= img[y:y+h x:x+h] h= 높이 관심영역지정 numpy 슬라이싱

import cv2 as cv
import numpy as np
img= cv.imread('../../img/Lenna.png')

x=320; y=150; w=50; h=50 # roi 좌표
roi = img[y:y+h, x:x+h]

print(roi.shape)
cv.rectangle(roi,(0,0),(x+w,y+h), (0,255,0))
cv.imshow('img',img)

cv.waitKey(0)
cv.destroyAllWindows()
