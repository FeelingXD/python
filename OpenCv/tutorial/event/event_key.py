import cv2 as cv
img_file = '../../img/Lenna.png'
img = cv.imread(img_file)
title = 'IMG'
x,y=100,100

while True:
    cv.imshow(title,img)
    cv.moveWindow(title, x, y)
    key =cv.waitKey(0) & 0xFF
    print(key,chr(key))
    if key == ord('h'):
        x-=10
    elif key == ord('j'):
        y+=10
    elif key == ord('k'):
        y-=10
    elif key == ord('l'):
        x+=10
    elif key == ord('q') or key== 27:
        break
        cv.destroyAllWindows()
    cv.moveWindow(title,x,y)
