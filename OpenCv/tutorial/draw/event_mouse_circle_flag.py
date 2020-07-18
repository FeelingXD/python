import cv2 as cv

title  = 'mouse event'
img = cv.imread('../../img/blankimg.png')
cv.imshow(title,img)

colors = {'black':(0,0,0),
            'red':(0,0,255),
            'blue':(255,0,0),
            'green':(0,255,0)}# 색상정의

def onMouse(event,x,y,flags,param):
    print(event,x,y,flags)
    color = colors['black']
    if event== cv.EVENT_LBUTTONDOWN:
        if flags & cv.EVENT_FLAG_SHIFTKEY and flags & cv.EVENT_FLAG_CTRLKEY:
            color= colors['green']
        elif flags & cv.EVENT_FLAG_SHIFTKEY:
            color= colors['blue']
        elif flags & cv.EVENT_FLAG_CTRLKEY:
            color= colors['red']
        cv.circle(img, (x,y), 20,color,-1)
        cv.imshow(title,img)

cv.setMouseCallback(title,onMouse)
while True:
    if cv.waitKey(0)&0xff == 27:
        cv.destoryAllWindows()
