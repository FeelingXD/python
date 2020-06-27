#Goal
#1.read   image from file *using cv::imread)
#2. display an image in an opencv window(using  cv::imshow)
# 3. write image to file (using cv ::imwirte)

import cv2 as cv
import sys
img = cv.imread("C:\\Users\\ghpro\\Pictures\\Saved Pictures\\center_article_img.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
