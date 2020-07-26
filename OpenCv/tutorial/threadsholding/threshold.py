import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

img = cv.imread('../../img/Lenna.png', cv.IMREAD_GRAYSCALE )

thresh_np = np.zeros_like(img)
thresh_np[ img>127]=255

ret, thresh_cv = cv.threshold(img,127,255,cv.THRESH_BINARY)
print(ret)

imgs = {'original': img, 'Numpy API':thresh_np, 'cv.threshold': thresh_cv}
for i , (key,value) in enumerate(imgs.items()):
        plt.subplot(1,3,i+1)
        plt.title(key)
        plt.imshow(value, cmap='gray')
        plt.xticks([]); plt.yticks([])
plt.show()
