import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

img = cv.imread('../../img/Lenna.png',cv.IMREAD_GRAYSCALE)

_,t_bin= cv.threshold(img, 127,255, cv.THRESH_BINARY)
_,t_bininv= cv.threshold(img, 127,255, cv.THRESH_BINARY_INV)

imgs ={'origin':img, 'BINARY':t_bin, 'BINARY_INV':t_bininv}

for i, (key,value) in enumerate(imgs.items()):
    plt.subplot(2,3,i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]);plt.yticks([])

plt.show()
