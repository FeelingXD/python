import cv2 as cv
title = 'mouse event'
img = cv.imread ('../../img/Lenna.png')
cv.imshow(title,img)

def onMouse(event,x,y,flags,param): #callback func
    print(event,x,y, )
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),30,(0,0,0), -1)
        cv.imshow(title,img)

cv.setMouseCallback(title,onMouse)

while True:
    if cv.waitKey(0)&0xff ==27:
        break
cv.destroyAllWindows()
