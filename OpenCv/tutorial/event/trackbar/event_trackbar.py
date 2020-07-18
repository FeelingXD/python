import cv2 as cv
import numpy as np

win_name = 'Trackbar'

img = cv.imread('../../../img/blankimg.png')
cv.imshow(win_name,img)

def onChange(x):
    print(x)
    # R G B trackbar value
    r = cv.getTrackbarPos('R',win_name)
    g = cv.getTrackbarPos('G',win_name)
    b = cv.getTrackbarPos('B',win_name)
    print(r,g,b)
    img[:] = [b,g,r]
    cv.imshow(win_name,img)

# trackbar
cv.createTrackbar('R',win_name ,255,255,onChange)
cv.createTrackbar('G',win_name ,255,255,onChange)
cv.createTrackbar('D',win_name ,255,255,onChange)

while True:
    if cv.waitKey(1) & 0xFF ==27:
        break
cv.destroyAllWindows()
