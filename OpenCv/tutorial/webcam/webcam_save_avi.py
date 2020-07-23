import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'XVID')

#컬러
writer_c = cv.VideoWriter('../../video/output.avi',fourcc,30.0,(width,height))
#그래이
# writer_g = cv.VideoWriter('output.avi',fourcc,30.0,(width,height),0)
while True:
    ret,img = cap.read()

    if ret ==False:
        break

    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    cv.imshow('color',img)
    cv.imshow('gray',img_gray)

    writer_c.write(img)

    if cv.waitKey(1)&0xff == 27: ## 0xff == esc
        break

cap.release() #연결종료
writer_c.release()#연결종료
cv.destroyAllWindows()
