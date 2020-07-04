# -*- coding : cp989 -*-#
# -*- coding : utf-8 -*-#
import cv2 as cv #open cv
import numpy as np # numpy 행렬 계산

def grayscale(img): # 흑백화
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)
def canny(img, low_threshold, high_threshold): #canny algo
    return cv.Canny(img,low_threshold,high_threshold)
def gaussian_blur(img,kernel_size): # gaussian_blur
    return cv.GaussianBlur(img,(kernel_size, kernel_size),0)
