import cv2 as cv

img = cv.imread('../../img/blankimg.png')
#circle(img,원점 좌표, 반지름 ,라인색,굵기)
cv.circle(img,(150,150),100,(255,0,0))
cv.circle(img,(300,150),70,(0,255,0) ,5)
cv.circle(img,(400,150),50,(0,0,255),-1)#-1시 색채우기
#ellipse() 타원그리기
cv.ellipse(img,(50,300),(50,50),0,0,360,(0,0,255)) # 일반원 0 0 360 => 회전, 시작각, 종료각 0회전각 0도부터 360 까지 조건사항으로 타원그리기
cv.ellipse(img,(150,300),(50,50),0,0,180,(255,0,0)) # 아래 반원그리기
cv.ellipse(img,(200,300),(50,50),0,181,360,(0,255,0),2)


cv.imshow('circle',img)
cv.waitKey(0)
