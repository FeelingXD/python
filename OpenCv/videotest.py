# Goal
# read video display video and save video
# capture video from a  camera and display it
# cv.VideoCapture(), cv.VideoWrite()

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('cannot use camera')
    exit()
while True:
    #VideoCapture frame
    ret, frame = cap.read()
    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
    #Our operation on the frame is read
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #display result frame
    cv.imshow('frame',gray)
    if cv.waitKey(1)==ord('q'):
        break
# when everything done realese the VideoCapture
cap.release()
cv.destroyAllWindowsWindow()
