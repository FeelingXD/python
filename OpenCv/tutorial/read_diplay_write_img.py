#Goal
#1.read   image from file *using cv::imread)
#2. display an image in an opencv window(using  cv::imshow)
# 3. write image to file (using cv ::imwirte)

import cv2 as cv
import sys
img = cv.imread("C:\\Users\\ghpro\\Pictures\\Saved Pictures\\center_article_img.jpg")
# cv.imread (경로,flag) falg default=color options =
# cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.
# cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다.
# cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다.
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
