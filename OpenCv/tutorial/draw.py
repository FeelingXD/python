import cv2 as cv
import numpy as np

img =cv.imread('../img/Lenna.png')
cv.imshow('asdf',img)
k= cv.waitKey(0)
if k==ord('q'):
    cv.imwrite('war',img)
