#ROI REGION OF INTEREST 관심영역 설정하기 .MASK 를이용하여 만듦
#img 이용
#moustcall back 이용
import numpy as np
import cv2 as cv

mouse_is_pressing= False
start_x, start_y=-1,-1

def mouse_callback(event,x,y,flags,param):
    global start_x,start_y,mouse_is_pressing
    img_result =img_color.copy()

    if event == cv.EVENT_LBUTTONDOWN:
        mouse_is_pressing=True
        start_x,start_y=x,y
        cv.circle(img_result,(x,y),10,(0,255,0),-1)
        cv.imshow("img_color",img_result)

    elif event == cv.EVENT_MOUSEMOVE:
        if mouse_is_pressing:
            cv.rectangle(img_result,(start_x,start_y),(x,y),(0,255,0),3)
            cv.imshow("img_color",img_result)

    elif event == cv.EVENT_LBUTTONUP:
        mouse_is_pressing=False
        img_land = img_color[start_y:y,start_x:x]
        img_land = cv.cvtColor(img_land,cv.COLOR_BGR2GRAY)
        img_land = cv.cvtColor(img_land,cv.COLOR_GRAY2BGR)
        cv.imshow("img_color", img_result)
        cv.imshow("img_land",img_land)

img_color = cv.imread('../../img/solidWhiteCurve.jpg',cv.IMREAD_COLOR)
cv.imshow('img_color',img_color)
cv.setMouseCallback('img_color',mouse_callback)

cv.waitKey(0)
cv.destroyAllWindows()
