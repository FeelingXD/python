import cv2 as cv
import numpy as np

video = cv.VideoCapture("../video/ride.mp4")
while True:
    if(video.get(cv.CAP_PROP_POS_FRAMES)==video.get(cv.CAP_PROP_FRAME_COUNT)):
        video.open('../video/ride.mp4') #영상 끝 도달시 다시반복재생

    ret, frame = video.read()
    cv.imshow('Video',frame)

    if cv.waitKey(11)>0: break

video.release()
cv.destroyAllWindows()
