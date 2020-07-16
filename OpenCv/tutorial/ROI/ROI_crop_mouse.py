import cv2 as cv
import numpy as np

isDragging = False#드래그상태
x0,y0,w,h=-1,-1,-1,-1#영역 선택 좌표
blue,red = (255,0,0),(0,0,255)#생상값

def onMouse(event,x,y,flags,param):#마우스이밴트 핸들
    global isDragging, x0, y0, img
    if event==cv.EVENT_LBUTTONDOWN:
        isDragging=True
        x0=x
        y0=y
    elif event == cv.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw =img.copy()
            cv.rectangle(img_draw,(x0,y0),(x,y),blue,2)#드래그영역
            cv.imshow('img',img_draw)
    elif event == cv.EVENT_LBUTTONUP:
        if isDragging:
            isDragging:False
            w=x-x0
            h=y-y0
            print('x:%d, y:%d, w:%d, h:%d'% (x0,y0,w,h))
            if w>0 and h>0:
                img_draw = img.copy()

                cv.rectangle(img_draw,(x0,y0), (x,y), red ,2)
                cv.imshow('img',img_draw)
                roi = img[y:y0+h,x0:x0+w]
                cv.imshow('cropped',roi)
                cv.moveWindow('cropped',0,0)
                cv.imwrite('../../img/cropped.png',roi)
                print("cropped.")
            else:
                # if wrong use this func it will show raw img
                cv.imshow('img',img)
                print("좌측상단에서 우측하단으로 드래그 하시오.")
img= cv.imread('../../img/Lenna.png')
cv.imshow('img',img)
cv.setMouseCallback('img',onMouse)# use mouse callback func
cv.waitKey()
cv.destroyAllWindows()
